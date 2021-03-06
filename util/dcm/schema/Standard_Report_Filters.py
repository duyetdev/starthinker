###########################################################################
#
#  Copyright 2017 Google Inc.
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

Standard_Report_Filters_Schema = [
  { "name":"Activity", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad_Status", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Attributed_Event_Connection_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Attributed_Event_Environment", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Browser_Platform", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_End_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_External_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_Start_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"City", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Click_Through_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Companion_Creative", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Companion_Creative_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Connection_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Content_Category", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Content_Classifier", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_End_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_6", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_7", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_8", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_9", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_10", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_11", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Field_12", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Groups_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Groups_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Start_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Digital_Content_Label", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Designated_Market_Area_Dma", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Domain", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Field_Value_6", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Environment", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Attributed_Event_Platform_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Configuration", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Hour", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Mobile_Carrier", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Property", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Landing_Page", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Landing_Page_Query_String", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Processed_Landing_Page", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Processed_Landing_Page_Query_String", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Query", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Total_Booked_Units", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Agency", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Bid_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Campaign", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Keyword", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Landing_Page_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Payment_Source", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Compatibility", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Cost_Structure", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_External_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Tag_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Total_Booked_Units", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Platform_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rendering_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Site_Dcm", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Site_Directory", "type":"STRING", "mode":"NULLABLE" },
  { "name":"State_Region", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List_Description", "type":"STRING", "mode":"NULLABLE" },
  { "name":"User_List_Membership_Life_Span", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Video_Player_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Video_Prominence_Score", "type":"STRING", "mode":"NULLABLE" }
]