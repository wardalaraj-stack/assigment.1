HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command: python harborflow_app.py
Python version tested: Python 3.14.7 (menu smoke test)

Team members and concrete contributions
---------------------------------------
Name: Raydel Savón Hernández
Contribution:
 Implemented Task 1 (Build the dispatch menu), including the persistent main
  menu, menu selection handling, conditional dispatch to the corresponding
  service functions, and closing the console through loop state rather than
  using exit().
- Structured the menu so that each service is called through its corresponding
  function and control returns safely to the main menu after a service finishes.
- Implemented Task 2 (Validate booking reference), including normalization of
  user input and validation of the required HFL-CCC-NNNN structure.
- Implemented checks for the fixed HFL prefix, exact reference length, required
  hyphen positions, three-letter customer code, and four-digit shipment number
  without using regular expressions.
- Implemented the repeated validation flow for Task 2 so that invalid booking
  references are rejected and the user is prompted again without being returned
  prematurely to the main menu.
- Tested Tasks 1 and 2 against the assignment requirements, including menu
  dispatch, return-to-menu behavior, controlled console closing, lowercase and
  whitespace normalization, incorrect reference length, misplaced hyphens,
  invalid customer codes, invalid shipment numbers, and invalid-to-valid
  recovery.
- Recorded the Task 1 and Task 2 test results in the team's shared test ledger,
  with all tested cases passing.
- Participated in the final testing of the integrated HarborFlow Dispatch
  Console, checking the combined application after the individual task
  implementations had been brought together.
- Participated in the final integration and merge of the team's work into the
  shared console and helped verify that the integrated application worked as
  one complete program.
- Coordinated much of the team's practical collaboration by arranging meeting
  dates, communicating availability, and booking places for in-person team
  meetings.

Name: Abdalsalam Ward Alaraj
Contribution:
- Served as the technical lead by coordinating the integration of the separate task 
implementations into the main application.
- Designed the overall structure of the HarborFlow Dispatch Console 
and organized the project into task-specific implementation and review files.
- Created and maintained the task checklists used to track progress across Tasks 1-9.
- Created the detailed task instruction files describing the required inputs, 
calculations, outputs, validation rules, testing checklists, and acceptance criteria.
- Created the allowed-tools and limitations guide to keep the solution within the 
assignment's permitted Python scope.
- Created the shared functions and variables reference so the team could use 
consistent names, boundaries, and calculations across the application.
- Independently implemented Task 3, including positive-number validation, 
service-code validation, service names, the delivery-quote formula, and 
formatted quote output.
- Independently implemented Task 9, including comparison of Standard, Express, 
and Priority services, reuse of the shared quote calculation, price formatting, 
and cheapest/most-expensive service selection.
- Hosted and managed the project repository, including branch coordination, merging 
team changes, and maintaining the shared project state.
- Stress-tested the application and checked normal, boundary, and invalid-input 
cases across the required tasks.
- Reviewed the implementation against the allowed-tools and limitations guide, 
including restrictions on dictionaries, files, regular expressions, sets, 
list comprehensions, classes, third-party packages, and exit().
- Validated the work submitted by group members and integrated the completed 
task implementations into the final console structure.

Name: Waldean Nelson
Contribution: 
- Implemented Task 6 (Classify service performance): reads promised
  minutes, actual minutes and damaged parcels, calculates the delay and
  applies the decision table in order, with damage taking priority over
  timing. Includes validation so negative values are rejected and only
  the affected prompt repeats.
- Implemented Task 7 (Produce weekly dispatch report): reads and
  validates seven daily delivery counts and a target, then calculates
  the total, average, highest/lowest day (last day wins on ties) and
  days meeting the target without using max(), min(), sum() or index().
- Wrote a script to create and validate entries in test-ledger.csv,
  and wrote the boundary and validation test cases for Tasks 6 and 7.
- Set up the team's GitHub repository and introduced the group to it
  for version control and integrating each member's code.
- Set up a Trello board to track task ownership and monitor the
  group's progress.

Name (if applicable): [Confirm fourth member]
Contribution: [Add concrete contribution before submission.]

Design notes
------------
Main function boundaries: main() displays the persistent menu and dispatches each option to a service function. Each service handles its own inputs, calculations, and output. Helpers such as calculate_quote() and the weekly-report calculation functions separate reusable logic.
How input validation is organized: read_menu_choice() validates menu selections. Service-specific helper functions validate positive values, non-negative values, service codes, parcel weights, and weekly counts, repeating invalid prompts until valid input is supplied.
How shared calculations are reused: calculate_quote(distance, weight, service_code) contains the shared pricing formula and is called by both the delivery-quote service and the Task 9 comparison service. Weekly totals, target counts, and high/low day positions are calculated by separate helper functions.

Known limitations
-----------------
Task 3 and Task 9 need output-format review against the PDF contract. Confirm all group member names and contributions above.
