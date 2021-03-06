###########################################################################
# 
#  Copyright 2018 Google Inc.
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


from starthinker.util.project import project
from starthinker.util.google_api import API
from starthinker.util.data import put_rows


@project.from_parameters
def google_api():
  if project.verbose: print 'GOOGLE_API', project.task['api'], project.task['version']

  results = API(project.task).execute()

  put_rows(
    project.task['auth'], 
    project.task['out'], 
    '%s_%s.json' % (project.task['function'].replace('.', '_'), project.date), 
    results
  )


if __name__ == "__main__":
  google_api()
