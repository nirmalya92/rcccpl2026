
RCC CPL 2026 FULL FLASK PROJECT
===============================

A full unzip-and-run Flask project for RCC CPL 2026 using the premium dark-glass championship design language,
with a stronger index page structure and a dynamic responsive gallery.

RUN LOCALLY
-----------
1. Unzip anywhere, for example:
   C:\RCCCPL2026\RCC

2. Open terminal in that folder

3. Install dependencies:
   pip install -r requirements.txt

4. Start:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000

EDIT CONTENT
------------
You can edit page-by-page:
- templates/index.html
- templates/semi_finals.html
- templates/qf_results.html
- templates/leaderboard.html
- templates/appreciation.html
- templates/gallery.html
- templates/road_to_final.html

Shared layout:
- templates/base.html

Central data:
- app.py

ADD LOGOS
---------
Put images in:
static/logos/

Suggested:
- rcc_logo.png

ADD GALLERY PHOTOS
------------------
Put any .jpg / .jpeg / .png / .webp files in:
static/photos/

They will automatically appear in the Gallery page.

WINDOWS QUICK RUN
-----------------
You can also double-click:
run_project.bat
