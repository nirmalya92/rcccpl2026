from pathlib import Path
from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent
PHOTOS_DIR = BASE_DIR / "static" / "photos"

app = Flask(__name__)

SITE = {
    "title": "RAILVIHAR CRICKET CLUB PRESENTS CPL 2026",
    "full_title": "RCC Corporate Premier League 2026",
    "tagline": "Red Leather. Real Rivalry.",
    "subtext": "Odisha's premier corporate red leather cricket league",
    "hero_support": "4 April 2026 • CVRAMAN Cricket Ground • The Final Four Are Ready",

    "home_stats": [
        {"icon": "🏏", "value": "15", "label": "Teams"},
        {"icon": "📍", "value": "2", "label": "Premium Grounds"},
        {"icon": "🎥", "value": "LIVE", "label": "YouTube"},
        {"icon": "📊", "value": "LIVE", "label": "CricHeroes"},
        {"icon": "🍽️", "value": "FULL", "label": "Match Setup"},
    ],

    "about": {
        "headline": "About The League",
        "text": "RCC CPL 2026 is Odisha's first structured corporate red leather cricket league, bringing together top corporate teams in a professionally managed competitive environment.",
        "points": [
            "Group + Knockout Format",
            "Professional Umpiring",
            "Organized Match Operations"
        ],
    },

    "live_action": {
        "live_match": {
            "status": "No live match right now",
            "detail": "The next live update will appear here during match hours. Until then, recent results and highlights keep the page active."
        },
        "recent_results": [
            "CCC defeated TCC by 7 wickets",
            "Royal Rangers defeated KIIT by 4 wickets",
            "Corporate Invitation XI defeated Bhubaneswar Startup XI by 6 wickets",
            "X Riders Commendable Veterans defeated ECC by 16 runs",
        ],
        "top4": [
            {"team": "CCC", "rank": 1},
            {"team": "Royal Rangers", "rank": 2},
            {"team": "Corporate Invitation XI", "rank": 3},
            {"team": "X Riders Commendable Veterans", "rank": 4},
        ],
        "videos": [
            "Knockout Highlights",
            "Captain Bytes",
            "Short Reels",
        ],
    },

    "featured_match": {
        "title": "Upcoming Match",
        "teams": "Royal Rangers vs Corporate Invitation XI",
        "time": "4 April 2026 • 1st Match",
        "ground": "CVRAMAN Cricket Ground",
        "countdown_note": "Countdown timer area ready for future enhancement",
    },

    "schedule_preview": [
        {"match": "Royal Rangers vs Corporate Invitation XI", "time": "4 Apr • 1st Match", "ground": "CVRAMAN"},
        {"match": "CCC vs X Riders Commendable Veterans", "time": "4 Apr • 2nd Match", "ground": "CVRAMAN"},
        {"match": "Semi Final Winner 1 vs Semi Final Winner 2", "time": "Final • TBD", "ground": "TBD"},
        {"match": "Highlights & Presentation", "time": "Post Match", "ground": "Main Stage"},
    ],

    "team_showcase_cards": [
        {"name": "CCC", "file": "ccc.png"},
        {"name": "Commendale Veterans", "file": "commendable_veterans.png"},
        {"name": "Corporate Invitation XI", "file": "corporate_invitation_xi.png"},
        {"name": "ECC", "file": "ecc.png"},
        {"name": "Kalinga Warriors", "file": "kalinga_warriors.png"},
        {"name": "KIIT", "file": "kiit.png"},
        {"name": "Mavericks", "file": "mavericks.png"},
        {"name": "Orissa Lawyers Cricket Association", "file": "orissa_lawyers_cricket_association.png"},
        {"name": "RCC", "file": "rcc.png"},
        {"name": "Resolute Cricket Club", "file": "resolute_cricket_club.png"},
        {"name": "Royal Rangers", "file": "royal_rangers.png"},
        {"name": "S3C", "file": "s3c.png"},
        {"name": "Startup XI", "file": "startup_xi.png"},
        {"name": "TCC", "file": "tcc.png"},
        {"name": "Utkal Spartans", "file": "utkal_spartans.png"},
    ],

    "media_cards": [
        {
            "title": "Match Highlights",
            "text": "Watch full match highlights and live coverage archives from our YouTube playlist.",
            "url": "https://youtube.com/playlist?list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&si=0CjTcxQ7maa3VtaV",
            "link_label": "Open YouTube Playlist ↗"
        },
        {
            "title": "Captain Bytes",
            "text": "Explore captain reactions, pre-match thoughts, and post-match bytes on Instagram.",
            "url": "https://www.instagram.com/rail_rockerz/",
            "link_label": "Open Instagram Page ↗"
        },
        {
            "title": "Short Reels",
            "text": "Watch short-form reels, quick highlights, and social-ready tournament moments on Instagram.",
            "url": "https://www.instagram.com/rail_rockerz/",
            "link_label": "Open Instagram Reels ↗"
        },
    ],

    "sponsors": [
    {
        "name": "3rd Eye Vidyuts",
        "role": "Title Sponsor",
        "file": "3rd_eye_vidyuts.png"
    },
    {
        "name": "AK143",
        "role": "Broadcasting Partner",
        "file": "ak143.png"
    },
    {
        "name": "Rivosolar",
        "role": "Hospitality Partner",
        "file": "rivosolar.png"
    },
    {
        "name": "Gopabandhu Cricket Club",
        "role": "Trophy Partner",
        "file": "gopabandhu_cricket_club.png"
    },
    {
        "name": "Kruti Coffee",
        "role": "Supported By",
        "file": "kruti_coffee.png"
    },
    ],

    "grounds": [
        {"name": "CV RAMAN", "desc": "Championship matchday venue with premium knockout atmosphere."},
        {"name": "IDCO", "desc": "Competitive ground that helped shape the road to the semi-finals."},
    ],

    "announcements": [
        "Schedule updates will be posted here first.",
        "Weather alerts and matchday notices will appear here.",
        "Operational changes can be announced without WhatsApp chaos.",
    ],

    "contact": {
        "name": "RCC CPL Organizing Team",
        "phone": "8861221172",
        "email": "railviharcricketclub@gmail.com",
        "cta": "Join / Partner With Us",
    },

    "semi_finals": [
    {
        "name": "Semi Final 1",
        "team1": "Royal Rangers",
        "team2": "Corporate Invitation XI",
        "team1_logo": "teams/royal-rangers-logo.png",
        "team2_logo": "teams/cixi-logo.png",
        "banner": "semifinals/sf1-banner.jpg",
        "slot": "CVRAMAN • 1st Match",
        "date_line": "4 April 2026",
        "venue": "CVRAMAN",
        "toss_time": "8:30 AM",
        "start_time": "8:45 AM",
        "match_code": "RCC-CPL26-SF1",
        "overs": "20 Overs",
        "ball_type": "Red Leather",
        "path": "Winner of QF2 vs Winner of QF3"
    },
    {
        "name": "Semi Final 2",
        "team1": "CCC",
        "team2": "X Riders Commendable Veterans",
        "team1_logo": "teams/ccc-logo.png",
        "team2_logo": "teams/xrcv-logo.png",
        "banner": "semifinals/sf2-banner.jpg",
        "slot": "CVRAMAN • 2nd Match",
        "date_line": "4 April 2026",
        "venue": "CVRAMAN",
        "toss_time": "12:15 PM",
        "start_time": "12:30 PM",
        "match_code": "RCC-CPL26-SF2",
        "overs": "20 Overs",
        "ball_type": "Red Leather",
        "path": "Winner of QF1 vs Winner of QF4"
    },
    ],

    "qf_results": [
    {
        "tag": "QF1",
        "meta": "CV RAMAN Cricket Ground, Bhubaneswar • 29-Mar-2026 • 20 Ov.",
        "team1": "CCC",
        "team1_score": "132/3 (14.4)",
        "team2": "TCC (The Corporate Cricketers)",
        "team2_score": "129/10 (20.0)",
        "winner_side": "left",
        "summary": "CCC won by 7 wickets",
        "moment": "Tanmoy Parida’s sensational hat-trick blew the game apart and turned the quarter-final decisively in CCC’s favour.",
        "mom": {
            "name": "Tanmoy Parida",
            "profile_url": "https://chshare.link/player/nmLK73",
            "performance": "Tanmoy Parida produced the defining spell of the quarter-final, claiming a sensational hat-trick and finishing with 4 for 25 in his 4 overs."
        },
        "match_link": "https://cricheroes.com/scorecard/23493704/rcc-corporate-premier-league-2026/tcc-(the-corporate-cricketers)-vs-ccc/summary",
        "youtube_links": [
            "https://www.youtube.com/watch?v=WDlbh4ZZ78U"
        ]
    },
    {
        "tag": "QF2",
        "meta": "IDCO Cricket Ground, Bhubaneswar • 29-Mar-2026 • 20 Ov.",
        "team1": "Royal Rangers",
        "team1_score": "79/6 (17.0)",
        "team2": "KIIT",
        "team2_score": "78/10 (18.2)",
        "winner_side": "left",
        "summary": "Royal Rangers won by 4 wickets",
        "moment": "In a tense low-scoring battle, Debasis Barik held his nerve with the bat and then strangled KIIT with a match-defining spell.",
        "mom": {
            "name": "Debasis Barik",
            "profile_url": "https://chshare.link/player/oa0gXe",
            "performance": "It was Debasis Barik who held his nerve brilliantly — an unbeaten 17 off 24 under pressure, followed by a magnificent 3 for 9 with the ball."
        },
        "match_link": "https://cricheroes.com/scorecard/23493793/rcc-corporate-premier-league-2026/kiit-vs-royal-rangers/summary",
        "youtube_links": [
            "https://www.youtube.com/watch?v=K6RVY4wB14A&list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&index=2&t=2882s&pp=iAQB"
        ]
    },
    {
        "tag": "QF3",
        "meta": "CV RAMAN Cricket Ground, Bhubaneswar • 29-Mar-2026 • 20 Ov.",
        "team1": "Corporate Invitation XI",
        "team1_score": "167/4 (19.2)",
        "team2": "Bhubaneswar Start Up XI",
        "team2_score": "166/10 (19.1)",
        "winner_side": "left",
        "summary": "Corporate Invitation XI won by 6 wickets",
        "moment": "Soumya Ranjan Nayak changed the tempo of the contest in a matter of overs and left his imprint on both innings.",
        "mom": {
            "name": "Soumya Ranjan Nayak",
            "profile_url": "https://chshare.link/player/mvVuhG",
            "performance": "Soumya Ranjan Nayak left his mark all over the game — a fiery 39 off 17 and a crucial 3 for 19 to seal a complete all-round performance."
        },
        "match_link": "https://cricheroes.com/scorecard/23493772/rcc-corporate-premier-league-2026/bhubaneswar-start-up-xi-vs-corporate-invitations-x1/summary",
        "youtube_links": [
            "https://www.youtube.com/watch?v=FUSU-iblDJk&list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&index=2&t=675s"
        ]
    },
    {
        "tag": "QF4",
        "meta": "IDCO Cricket Ground, Bhubaneswar • 29-Mar-2026 • 20 Ov.",
        "team1": "X Riders Commendable Veterans",
        "team1_score": "166/7 (20.0)",
        "team2": "ECC",
        "team2_score": "150/8 (20.0)",
        "winner_side": "left",
        "summary": "X Riders Commendable Veterans won by 16 runs",
        "moment": "Soumya Samal delivered the complete knockout performance, making his runs count and then tightening the screws with the ball.",
        "mom": {
            "name": "Soumya Samal",
            "profile_url": "https://chshare.link/player/mcLzH9",
            "performance": "A complete all-round display from Soumya Samal, who made 30 off 25 and then ran through the opposition with 3 for 11 in his 4 overs."
        },
        "match_link": "https://cricheroes.com/scorecard/23493747/rcc-corporate-premier-league-2026/x-riders-commendable-veterans-vs-ecc/summary",
        "youtube_links": [
            "https://www.youtube.com/watch?v=IehwTzhB1xE&list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&index=3&t=10s&pp=iAQB",
            "https://www.youtube.com/watch?v=Qng29Fjy2BE&list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&index=5&t=2s"
        ]
    },
        {
            "tag": "QF4",
            "meta": "IDCO Cricket Ground, Bhubaneswar • 29-Mar-2026 • 20 Ov.",
            "team1": "X Riders Commendable Veterans",
            "team1_score": "166/7 (20.0)",
            "team2": "ECC",
            "team2_score": "150/8 (20.0)",
            "winner_side": "left",
            "summary": "X Riders Commendable Veterans won by 16 runs",
            "mom": {
                "name": "Soumya Samal",
                "profile_url": "https://chshare.link/player/mcLzH9",
                "performance": "A complete all-round display from Soumya Samal, who made 30 off 25 and then ran through the opposition with 3 for 11 in his 4 overs."
            },
            "match_link": "https://cricheroes.com/scorecard/23493747/rcc-corporate-premier-league-2026/x-riders-commendable-veterans-vs-ecc/summary",
            "youtube_links": [
                "https://www.youtube.com/watch?v=IehwTzhB1xE&list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&index=3&t=10s&pp=iAQB",
                "https://www.youtube.com/watch?v=Qng29Fjy2BE&list=PLeRsXbAqkXBe1Zf8Recv74TmIPiwVNX-U&index=5&t=2s"
            ]
        },
    ],
    "leaderboard": {
        "mvp": {
            "name": "Ashok K Mallick",
            "team": "ECC",
            "desc": "MVP race leader with elite all-round influence and match impact.",
            "image": "images/players/ashok-k-mallick.png",
            "icon": "🏏",
            "stats": [
                {"value": "35.554", "label": "MVP Pts"},
                {"value": "266", "label": "Runs"},
                {"value": "5", "label": "Inns"},
            ]
        },
        "standouts": [
            {
                "icon": "🎯",
                "image": "images/players/tanmoy-parida.png",
                "name": "Tanmoy Parida",
                "role": "Top Bowler",
                "stats": [
                    {"value": "16", "label": "Wickets"},
                    {"value": "6.23", "label": "Eco"},
                    {"value": "50", "label": "Dots"},
                ],
                "note": "CCC"
            },
            {
                "icon": "🏏",
                "image": "images/players/ashok-k-mallick.png",
                "name": "Ashok K Mallick",
                "role": "Top Batter",
                "stats": [
                    {"value": "266", "label": "Runs"},
                    {"value": "66.5", "label": "Avg"},
                    {"value": "120.36", "label": "SR"},
                ],
                "note": "ECC"
            },
            {
                "icon": "⚡",
                "image": "images/players/acharya.png",
                "name": "Acharya",
                "role": "Power Performer",
                "stats": [
                    {"value": "201", "label": "Runs"},
                    {"value": "40.20", "label": "Avg"},
                    {"value": "164.75", "label": "SR"},
                ],
                "note": "X Riders Commendable Veterans"
            },
            {
                "icon": "🔥",
                "image": "images/players/lohit-mohanty.png",
                "name": "Lohit Mohanty",
                "role": "Batting Star",
                "stats": [
                    {"value": "225", "label": "Runs"},
                    {"value": "56.25", "label": "Avg"},
                    {"value": "156.25", "label": "SR"},
                ],
                "note": "Corporate Invitations X1"
            },
            {
                "icon": "💨",
                "image": "images/players/jeevan-dikhit.png",
                "name": "Jeevan Dikhit",
                "role": "Strike Bowler",
                "stats": [
                    {"value": "10", "label": "Wickets"},
                    {"value": "7.97", "label": "Eco"},
                    {"value": "8.1", "label": "Avg"},
                ],
                "note": "Corporate Invitations X1"
            },
            {
                "icon": "⭐",
                "image": "images/players/kabut-patel.png",
                "name": "Kabut Patel",
                "role": "Bowling Standout",
                "stats": [
                    {"value": "11", "label": "Wickets"},
                    {"value": "6.61", "label": "Eco"},
                    {"value": "46", "label": "Dots"},
                ],
                "note": "Bhubaneswar Start Up XI"
            },
        ]
    },

    "appreciation_sections": [
        {
            "emoji": "🏏",
            "title": "To All Participating Teams",
            "text": "Thank you for bringing intensity, preparation, and competitive spirit to the tournament. Your presence gave this league its energy, its quality, and its identity."
        },
        {
            "emoji": "🫡",
            "title": "To The Captains",
            "text": "Your leadership, coordination, and composure helped carry your teams through every challenge. The standard of discipline and communication set by you meant a great deal to the tournament."
        },
        {
            "emoji": "🎯",
            "title": "To The Players",
            "text": "Every run chased, every wicket taken, every dive in the field, and every moment of resilience added life to RCC CPL 2026. This tournament was richer because of your effort."
        },
        {
            "emoji": "🧾",
            "title": "To Umpires & Officials",
            "text": "Thank you for upholding the spirit of the game with fairness, patience, and professionalism. Your role was central in ensuring each contest was conducted with integrity."
        },
        {
            "emoji": "⚙️",
            "title": "To Organizers & Volunteers",
            "text": "Behind every scheduled fixture, prepared ground, update, and successful match stood your dedication. Much of what worked beautifully did so because of your unseen effort."
        },
        {
            "emoji": "🤝",
            "title": "To Sponsors, Partners & Supporters",
            "text": "Your trust and support added strength to the tournament journey. Your contribution helped us create something more meaningful, more professional, and more memorable."
        }
    ],

    "timeline": [
        {
            "title": "QUARTER-FINALS",
            "lines": [
                "CCC defeated TCC (7 wickets)",
                "Royal Rangers defeated KIIT (4 wickets)",
                "Corporate Invitation XI defeated Bhubaneswar Startup XI (6 wickets)",
                "X Riders Commendable Veterans defeated ECC (16 runs)",
            ],
        },
        {
            "title": "SEMI-FINALS",
            "lines": [
                "Semi-Final 1: Royal Rangers vs Corporate Invitation XI",
                "Semi-Final 2: CCC vs X Riders Commendable Veterans",
                "4 April 2026 • CVRAMAN Ground",
            ],
        },
        {
            "title": "FINAL",
            "lines": [
                "Championship Match • The Ultimate Prize",
                "Awaiting Semi-Final Winners",
            ],
        },
    ],
}

NAV = [
    ("Home", "home"),
    ("Semi Finals", "semi_finals"),
    ("QF Results", "qf_results"),
    ("Leaderboard", "leaderboard"),
    ("Appreciation", "appreciation"),
    ("Gallery", "gallery"),
    ("Road to Final", "road_to_final"),
]

def nav_links(active):
    return [{"label": label, "endpoint": endpoint, "active": endpoint == active} for label, endpoint in NAV]

def gallery_photos():
    allowed = {".jpg", ".jpeg", ".png", ".webp"}
    photos = []
    if PHOTOS_DIR.exists():
        for p in sorted(PHOTOS_DIR.iterdir()):
            if p.is_file() and p.suffix.lower() in allowed:
                photos.append({
                    "filename": p.name,
                    "title": p.stem.replace("_", " ").replace("-", " ").title()
                })
    return photos

def ctx(active):
    return {"site": SITE, "nav_links": nav_links(active), "photos": gallery_photos()}

@app.route("/")
def home():
    return render_template("index.html", **ctx("home"))

@app.route("/semi-finals")
def semi_finals():
    return render_template("semi_finals.html", **ctx("semi_finals"))

@app.route("/qf-results")
def qf_results():
    return render_template("qf_results.html", **ctx("qf_results"))

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", **ctx("leaderboard"))

@app.route("/appreciation")
def appreciation():
    return render_template("appreciation.html", **ctx("appreciation"))

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", **ctx("gallery"))

@app.route("/road-to-final")
def road_to_final():
    return render_template("road_to_final.html", **ctx("road_to_final"))

if __name__ == "__main__":
    app.run(debug=True)