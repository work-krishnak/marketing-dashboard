# Build Log — Marketing Analytics Dashboard

## Phase 2 — Marketing Analytics Dashboard

Live URL: https://marketing-dashboard-knzhpwcrcpbt7tuytz8uuo.streamlit.app/
GitHub repo: https://github.com/work-krishnak/marketing-dashboard
Status: Complete and verified live (checked in incognito browser too).

Issues encountered:
1. Terminal was occupied by the running Streamlit server (from local preview),
   couldn't run git commands until Ctrl+C stopped it.
2. Global git identity (name/email) was empty going into this phase, despite
   being set in Phase 0 -- Git auto-guessed an identity using the work machine
   (Krishna <v-kumarchak@microsoft.com>). Fixed by re-setting
   git config --global user.name/user.email and running
   git commit --amend --reset-author --no-edit before pushing.
3. Default branch was "master", renamed to "main" with git branch -M main
   to match GitHub's expected default and Streamlit Cloud's branch selection.

Time spent: approx 25 minutes including the identity troubleshooting.