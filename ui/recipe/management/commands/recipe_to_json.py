###########################################################################
# 
#  Copyright 2019 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

import pytz
import json
import pprint
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from starthinker.ui.ui.pubsub import send_message
from starthinker.ui.recipe.models import Recipe


class Command(BaseCommand):
  help = 'Moves database recipes to json files for cron consumption'

  def add_arguments(self, parser):
    parser.add_argument(
      '--remote',
      action='store_true',
      dest='remote',
      default=False,
      help='Run jobs remotely using pub sub.',
    )

    parser.add_argument(
      '--recipe',
      action='store',
      dest='recipe',
      default=None,
      help='Run a specific recipe.',
    )

    parser.add_argument(
      '--force',
      action='store_true',
      dest='force',
      default=False,
      help='Force execution regardless of schedule.',
    )


  def handle(self, *args, **kwargs):
    
    for recipe in (Recipe.objects.filter(pk=kwargs['recipe']) if kwargs['recipe'] else Recipe.objects.filter(active=True)):
      filename, data = recipe.get_json()

      print 'FILENAME:', filename
      #print 'JSON:', data
      #pprint.PrettyPrinter().pprint(data)

      # force by stripping time from setup
      if kwargs['force']:
        if 'day' in data['setup']: del data['setup']['day']
        if 'hour' in data['setup']: del data['setup']['hour']
      else:
        print "HAS SCHEDULE"

      # run the recipe using pub sub
      if kwargs['remote']:
        print 'EXECUTE REMOTE'
        print send_message(settings.UI_PROJECT, settings.UI_TOPIC, json.dumps(data))

      # save the recipe to a local file
      else:
        with open(filename, 'w') as outfile:
          json.dump(data, outfile)
