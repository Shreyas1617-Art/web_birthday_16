import streamlit as st
from streamlit_autorefresh import st_autorefresh
import os
import sys
from datetime import datetime
import base64
import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Happy Birthday Kushi",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Auto-refresh every 2s to cycle the shimmer phase on the title ────────────
_tick = st_autorefresh(interval=2000, limit=None, key="shimmer_refresh")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Raleway:wght@300;400;500&display=swap');
  html, body, [data-testid="stAppViewContainer"] { background: #0d0608 !important; font-family: 'Raleway', sans-serif; }
  [data-testid="stAppViewContainer"] {
    background:
      radial-gradient(ellipse 80% 60% at 50% -10%, rgba(180,40,60,0.28) 0%, transparent 70%),
      radial-gradient(ellipse 60% 40% at 80% 100%, rgba(120,20,40,0.22) 0%, transparent 60%),
      #0d0608 !important;
    min-height: 100vh;
  }
  [data-testid="stHeader"]  { background: transparent !important; }
  [data-testid="stToolbar"] { display: none !important; }
  footer { display: none !important; }
  .block-container { margin: 0 auto !important; padding-top: 2rem !important; padding-bottom: 4rem !important; max-width: 760px !important; }

  #petal-canvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }

  .hero { text-align: center; padding: 3.5rem 1rem 2rem; position: relative; z-index: 1; }
  .hero-subtitle { font-family: 'Raleway', sans-serif; font-weight: 300; letter-spacing: .45em; text-transform: uppercase; font-size: .72rem; color: rgba(220,160,140,0.75); margin-bottom: 1.1rem; animation: fadeUp .9s ease both; }
  .hero-title { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: clamp(2.6rem, 8vw, 4.4rem); color: #f5d9cf; line-height: 1.12; letter-spacing: .02em; margin: 0 0 .5rem; animation: fadeUp 1s .2s ease both; }
  .hero-title em { font-style: italic; color: #e8a09a; }
  .hero-date { font-family: 'Raleway', sans-serif; font-size: .78rem; font-weight: 400; letter-spacing: .3em; color: rgba(210,150,140,0.6); margin-top: .6rem; animation: fadeUp 1s .4s ease both; }

  .divider { display: flex; align-items: center; justify-content: center; gap: 1rem; margin: 2rem auto; max-width: 320px; animation: fadeUp 1s .5s ease both; }
  .divider-line { flex: 1; height: 1px; background: linear-gradient(to right, transparent, rgba(200,100,90,0.4), transparent); }

  .msg-card { background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, rgba(180,60,70,0.06) 100%); border: 1px solid rgba(200,100,90,0.18); border-radius: 2px; padding: 2.4rem 2.8rem; position: relative; z-index: 1; animation: fadeUp 1s .6s ease both; }
  .msg-card::before { content: '\201C'; font-family: 'Cormorant Garamond', serif; font-size: 6rem; line-height: 1; color: rgba(200,100,90,0.15); position: absolute; top: .4rem; left: 1.2rem; pointer-events: none; }
  .msg-text { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: clamp(1.05rem, 2.8vw, 1.22rem); color: #ecddd8; line-height: 1.88; text-align: center; position: relative; }
  .msg-sign { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1rem; color: rgba(220,160,140,0.65); text-align: right; margin-top: 1.4rem; }

  .reasons-title { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: 1.65rem; color: #f5d9cf; text-align: center; letter-spacing: .05em; margin: 3rem 0 1.6rem; animation: fadeUp 1s .7s ease both; }
  .reason-item { display: flex; align-items: flex-start; gap: 1rem; padding: .85rem 1rem; border-left: 1px solid rgba(200,100,90,0.25); margin-bottom: .85rem; animation: fadeUp 1s ease both; position: relative; z-index: 1; transition: border-color .3s; }
  .reason-item:hover { border-left-color: rgba(200,100,90,0.65); }
  .reason-num { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.4rem; color: rgba(200,100,90,0.5); min-width: 1.8rem; line-height: 1.3; }
  .reason-text { font-family: 'Raleway', sans-serif; font-weight: 300; font-size: .93rem; color: #d4c4bf; line-height: 1.7; }

  .countdown-wrap { text-align: center; margin: 2.8rem 0 1rem; position: relative; z-index: 1; animation: fadeUp 1s .9s ease both; }
  .countdown-label { font-family: 'Raleway', sans-serif; font-size: .68rem; letter-spacing: .4em; text-transform: uppercase; color: rgba(220,160,140,0.55); margin-bottom: 1.1rem; }
  .countdown-boxes { display: flex; justify-content: center; gap: 1.2rem; flex-wrap: wrap; }
  .cbox { background: rgba(255,255,255,0.03); border: 1px solid rgba(200,100,90,0.2); border-radius: 2px; padding: .7rem 1.2rem; min-width: 72px; }
  .cbox-num { font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 300; color: #e8a09a; line-height: 1; }
  .cbox-unit { font-family: 'Raleway', sans-serif; font-size: .6rem; letter-spacing: .25em; text-transform: uppercase; color: rgba(220,160,140,0.5); margin-top: .3rem; }

  .footer-wish { text-align: center; font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 1.1rem; color: rgba(220,160,140,0.55); margin-top: 3.5rem; position: relative; z-index: 1; animation: fadeUp 1s 1s ease both; }

  @keyframes fadeUp { from { opacity: 0; transform: translateY(22px); } to { opacity: 1; transform: translateY(0); } }

  /* ── Shining birthday title ── */
  .shine-title {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: clamp(1.6rem, 5vw, 2.4rem);
    text-align: center;
    letter-spacing: .12em;
    margin: 0 auto 0.2rem;
    position: relative; z-index: 2;
    background: linear-gradient(
      90deg,
      #c47c6a 0%,
      #f5d9cf 30%,
      #ffffff 48%,
      #ffe8e0 52%,
      #f5d9cf 70%,
      #c47c6a 100%
    );
    background-size: 220% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: titleShine 2.5s linear infinite;
    text-shadow: none;
    filter: drop-shadow(0 0 12px rgba(240,160,140,0.35));
  }
  @keyframes titleShine {
    0%   { background-position: 200% center; }
    100% { background-position: -200% center; }
  }

  /* ── Royal Photo Timeline ── */
  .timeline-wrap { position: relative; z-index: 1; margin: 3rem 0 2rem; }
  .timeline-title { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-style: italic; font-size: 1.7rem; color: #f5d9cf; text-align: center; margin-bottom: 2.5rem; letter-spacing: .06em; }

  .golden-line {
    position: absolute;
    left: 50%; top: 70px; bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom,
      transparent 0%, #b8860b 5%, #ffd700 20%,
      #ffe566 50%, #ffd700 80%, #b8860b 95%, transparent 100%);
    box-shadow: 0 0 6px 2px rgba(255,215,0,0.40), 0 0 18px 4px rgba(255,180,0,0.20);
    transform: translateX(-50%);
    border-radius: 2px;
  }

  .photo-row { display: flex; align-items: flex-start; gap: 2rem; margin-bottom: 3.5rem; position: relative; }
  .photo-row.right { flex-direction: row-reverse; }

  .spine-dot {
    position: absolute; left: 50%; top: 1.8rem;
    width: 13px; height: 13px;
    background: radial-gradient(circle, #fff8c0 0%, #ffd700 55%, #b8860b 100%);
    border-radius: 50%; transform: translateX(-50%);
    box-shadow: 0 0 12px 4px rgba(255,215,0,0.60); z-index: 2;
  }

  /* ── Plain photo box (no frame) ── */
  .photo-box { flex: 1; border-radius: 4px; overflow: hidden; }
  .photo-box img { width: 100%; display: block; object-fit: cover; max-height: 260px; }
  .photo-box .placeholder { height: 200px; display: flex; align-items: center; justify-content: center; background: rgba(255,215,0,0.04); font-family: 'Cormorant Garamond', serif; font-style: italic; color: rgba(255,215,0,0.25); font-size: .9rem; }

  .caption-box { flex: 1; padding-top: 3rem; }
  .caption-num { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 3rem; color: rgba(255,215,0,0.18); line-height: 1; margin-bottom: .4rem; }
  .caption-text { font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.05rem; color: #e8d5b0; line-height: 1.85; }
  .caption-sub { font-family: 'Raleway', sans-serif; font-size: .68rem; letter-spacing: .28em; text-transform: uppercase; color: rgba(255,200,80,0.42); margin-top: .7rem; }
</style>

<canvas id="petal-canvas"></canvas>
<script>
(function(){
  const canvas=document.getElementById('petal-canvas');
  const ctx=canvas.getContext('2d');
  let W,H,petals=[];
  function resize(){W=canvas.width=window.innerWidth;H=canvas.height=window.innerHeight;}
  resize(); window.addEventListener('resize',resize);
  const COLORS=['rgba(200,80,90,0.55)','rgba(220,120,110,0.45)','rgba(240,180,160,0.35)','rgba(180,50,70,0.5)'];
  function Petal(){this.x=Math.random()*W;this.y=-20;this.r=3+Math.random()*5;this.sp=.4+Math.random()*.8;this.sw=.4+Math.random()*.8;this.ang=Math.random()*Math.PI*2;this.rot=(Math.random()-.5)*.04;this.col=COLORS[Math.floor(Math.random()*COLORS.length)];this.t=0;}
  for(let i=0;i<28;i++){const p=new Petal();p.y=Math.random()*H;petals.push(p);}
  function draw(){ctx.clearRect(0,0,W,H);petals.forEach(p=>{p.t+=.016;p.y+=p.sp;p.x+=Math.sin(p.t*p.sw)*.7;p.ang+=p.rot;if(p.y>H+20){Object.assign(p,new Petal());}ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.ang);ctx.beginPath();ctx.ellipse(0,0,p.r,p.r*.55,0,0,Math.PI*2);ctx.fillStyle=p.col;ctx.fill();ctx.restore();});requestAnimationFrame(draw);}
  draw();
})();
</script>
""", unsafe_allow_html=True)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌹 Personalise")
    recipient = st.text_input("Their name", value="Kushi❤️")
    sender    = st.text_input("Your name",  value="Shreyas")
    bday_msg  = st.text_area("Your heartfelt message", value=(
        "On this beautiful day, I wish your dreams take flight and your heart finds endless reasons to smile, "
        "Thank you for simply being you, "
        "keep this smile for a lifetime."
    ), height=160)
    st.markdown("---")
    bday_date = st.date_input("Her birthday (for countdown)")

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <div class="hero-subtitle">A birthday letter, with all my heart</div>
  <div class="shine-title">✦ &nbsp; Happy Birthday, {recipient}  &nbsp; ✦</div>
  <div class="hero-date">🌹 &nbsp; Today is your day &nbsp; 🌹</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="divider">
  <div class="divider-line"></div>
  <span style="font-size:1rem">✦</span>
  <div class="divider-line"></div>
</div>
""", unsafe_allow_html=True)

# ── Message card ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="msg-card">
  <div class="msg-text">{bday_msg.replace(".", ".<br>")}</div>
  <div class="msg-sign">— {sender} 🌹</div>
</div>
""", unsafe_allow_html=True)

# ── Reasons (hardcoded, no sidebar loop) ──────────────────────────────────────
reasons = [
    "Your simplicity as a person ",
    "Your soft voice",
    "Your kindness ",
    "Being yourself",
]

st.markdown('<div class="reasons-title">What makes kushi special</div>', unsafe_allow_html=True)
for idx, reason in enumerate(reasons, 1):
    st.markdown(f"""
    <div class="reason-item" style="animation-delay:{0.7 + idx*0.1}s">
      <span class="reason-num">{idx:02d}</span>
      <span class="reason-text">{reason}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="divider" style="margin-top:2.5rem">
  <div class="divider-line"></div>
  <span style="font-size:1rem">✦</span>
  <div class="divider-line"></div>
</div>
""", unsafe_allow_html=True)

# ── Royal Photo Timeline ───────────────────────────────────────────────────────
def img_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_mime(path):
    ext = path.rsplit(".", 1)[-1].lower()
    return "jpeg" if ext in ("jpg", "jpeg") else ext

# ── Edit your photos & captions here ──
photo_list = [
    {
        "image_path": "pic2_red.jpg",
        "caption": "May your days be as bright, beautiful and full of love as this picture",
        "sub": "",
    },
    {
        "image_path": "pic3_white.jpg",
        "caption": "Even with the sunset in the background , brightest light is smile in this frame , may your radiant smile be as good as this moment  ",
        "sub": "",
    },
    {
        "image_path": "pic4_grey.jpg",
        "caption": "Be confident and keep that attitude as well as vibe throughout year as this pic",
        "sub": "",
    },
    {
        "image_path": "pic1_skyblue.jpg",
        "caption":  "I just want to describe this pic in my words so! Arz kiyaaa hai <br>"
                     "<br>"
                    "Aapka ankhoen ko dekhu toh aasman chota lagata hai,<br>"
                    "Yeh chamakta chaand , yeh sitaare sab dhoka lagta hai,<br>"
                    "Kaisa jaadoo hai aapke hasi mein aur aapke zulfoen main,<br>"
                    "Ki poori duniya saamne ho toh , phir bi yeh dil aap ko dundtha hai",
        "sub": "",
    },
]

st.markdown('<div class="timeline-wrap">', unsafe_allow_html=True)
st.markdown('<div class="timeline-title">Stay Happppppyyyy</div>', unsafe_allow_html=True)
st.markdown('<div class="golden-line"></div>', unsafe_allow_html=True)

for idx, p in enumerate(photo_list):
    side = "right" if idx % 2 == 1 else "left"

    if os.path.exists(p["image_path"]):
        mime  = get_mime(p["image_path"])
        b64   = img_to_b64(p["image_path"])
        inner = f'<img src="data:image/{mime};base64,{b64}" alt="moment">'
    else:
        inner = f'<div class="placeholder">add {p["image_path"]} to this folder</div>'

    caption_html = ""
    if p["caption"]:
        caption_html += f'<div class="caption-text">{p["caption"]}</div>'
    if p["sub"]:
        caption_html += f'<div class="caption-sub">{p["sub"]}</div>'

    st.markdown(f"""
    <div class="photo-row {side}">
      <div class="spine-dot"></div>
      <div class="photo-box">{inner}</div>
      <div class="caption-box">
        {caption_html}
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Countdown ─────────────────────────────────────────────────────────────────
today     = datetime.date.today()
next_bday = bday_date.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year + 1)
delta = next_bday - today

if delta.days == 0:
    st.markdown("""
    <div class="countdown-wrap">
      <div class="countdown-label">Finally i want to Say !</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:#e8a09a;font-style:italic;">
        Greatful to have you in my life , hope you have a wonderful year ahead 💗.
      </div>
    </div>
    """, unsafe_allow_html=True)
else:
    yrs  = delta.days // 365
    mths = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    st.markdown(f"""
    <div class="countdown-wrap">
      <div class="countdown-label">next birthday in</div>
      <div class="countdown-boxes">
        <div class="cbox"><div class="cbox-num">{yrs:02d}</div><div class="cbox-unit">Years</div></div>
        <div class="cbox"><div class="cbox-num">{mths:02d}</div><div class="cbox-unit">Months</div></div>
        <div class="cbox"><div class="cbox-num">{days:02d}</div><div class="cbox-unit">Days</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-wish">
  "May all your dream come true and may you be blessed with endless happiness and love. Happy Birthday once again💗"
</div>
""", unsafe_allow_html=True)