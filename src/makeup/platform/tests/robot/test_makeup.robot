# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s makeup.platform -t test_makeup.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src makeup.platform.testing.MAKEUP_PLATFORM_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_makeup.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a makeup
  Given a logged-in site administrator
    and an add makeup form
   When I type 'My makeup' into the title field
    and I submit the form
   Then a makeup with the title 'My makeup' has been created

Scenario: As a site administrator I can view a makeup
  Given a logged-in site administrator
    and a makeup 'My makeup'
   When I go to the makeup view
   Then I can see the makeup title 'My makeup'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add makeup form
  Go To  ${PLONE_URL}/++add++makeup

a makeup 'My makeup'
  Create content  type=makeup  id=my-makeup  title=My makeup


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the makeup view
  Go To  ${PLONE_URL}/my-makeup
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a makeup with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the makeup title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
