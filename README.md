# AIFRS #

Python using OpenAI Framework

# Development Workflow: #
Users branch off the Develop branch. Changes will be merged into Develop. Once a release shall occur,
Develop will be merged to Master and Master branch is released.

* *Create* an issue for planned work
* *Create* a branch for the issue off of Develop (feature/<issue#>-name-for-branch) eg: "feature/1-update-workflow"
* During development, commit messages should be prepended with issue number and comments relevant to work 
* Once work is done and committed, create a *Pull Request* and add team as reviewers. Description of work done should be added
* Once Pull Request has 3 approvals, the work can be *merged* into Develop.
* Once merged into Develop, close the appropriate *Issue*
* Once merged to develop, demo to lead and hand to test team to test the *specific feature*.
* Upon passing feature test, develop is OK to be merged to Master at any point.