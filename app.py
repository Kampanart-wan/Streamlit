import streamlit as st


st.set_page_config(
    page_title="Taskflow",
    page_icon="T",
    layout="wide",
    initial_sidebar_state="collapsed",
)

LANGUAGES = {
    "ไทย": "th",
    "English": "en",
    "日本語": "ja",
}

THEMES = {
    "Indigo": {
        "accent": "#5368d9",
        "accent_dark": "#3e51ba",
        "soft": "#edf0ff",
        "glow": "rgba(83, 104, 217, .10)",
        "background": "#f5f7fb",
        "ink": "#202b42",
        "muted": "#778198",
        "line": "#e6eaf1",
        "card": "rgba(255, 255, 255, .92)",
    },
    "Sage": {
        "accent": "#39816d",
        "accent_dark": "#286653",
        "soft": "#eaf5f0",
        "glow": "rgba(57, 129, 109, .10)",
        "background": "#f4f8f6",
        "ink": "#20362f",
        "muted": "#71847d",
        "line": "#e2ece7",
        "card": "rgba(255, 255, 255, .94)",
    },
    "Coral": {
        "accent": "#c7634d",
        "accent_dark": "#a94c38",
        "soft": "#fff0eb",
        "glow": "rgba(199, 99, 77, .10)",
        "background": "#fbf6f3",
        "ink": "#3c2b28",
        "muted": "#8c7771",
        "line": "#f0e5e0",
        "card": "rgba(255, 255, 255, .94)",
    },
}

TEXT = {
    "th": {
        "language": "ภาษา",
        "theme": "โทนสี",
        "hero_title": "จัดลำดับงานให้ชัด<br>แล้วเริ่มจากสิ่งสำคัญ",
        "hero_subtitle": "พื้นที่วางแผนที่เรียบง่าย ช่วยให้คุณโฟกัสกับงานถัดไปได้ทันที",
        "add_title": "เพิ่มงานใหม่",
        "add_caption": "ใส่รายละเอียด แล้วให้ Taskflow ช่วยจัดลำดับ",
        "task_name": "ชื่องาน",
        "task_placeholder": "เช่น เตรียมสไลด์นำเสนอ",
        "deadline": "กำหนดส่งในอีกกี่วัน",
        "deadline_help": "เลือกจำนวนวันเต็มตั้งแต่ 0–365 วัน (0 หมายถึงครบกำหนดวันนี้)",
        "importance": "ระดับความสำคัญ (1–5)",
        "importance_help": "ประเมินจากผลกระทบของงาน ไม่ใช่ความเร่งด่วน",
        "importance_level": ["น้อยมาก", "น้อย", "ปานกลาง", "สูง", "วิกฤต"],
        "importance_examples": [
            "งานเสริม หรือทำเมื่อมีเวลาว่าง",
            "มีประโยชน์ แต่เลื่อนได้",
            "เกี่ยวข้องกับงานหลักหรือเป้าหมาย",
            "สำคัญต่อผลลัพธ์หรือมีคนรออยู่",
            "ผลกระทบสูง ควรจัดการเป็นอันดับต้น",
        ],
        "all_levels": "ดูเกณฑ์ระดับความสำคัญ",
        "add_button": "เพิ่มงานเข้ารายการ",
        "added": "เพิ่มงานในรายการแล้ว",
        "empty_name": "กรุณากรอกชื่องานก่อน",
        "overview": "ภาพรวมงาน",
        "overview_caption": "โฟกัสงานสำคัญ และติดตามกำหนดส่งได้ในที่เดียว",
        "total": "งานทั้งหมด",
        "top_score": "คะแนนสูงสุด",
        "nearest": "กำหนดส่งใกล้สุด",
        "day_unit": "วัน",
        "rank": "ลำดับ",
        "importance_short": "ความสำคัญ",
        "due_in": "กำหนดส่งใน {days} วัน",
        "urgent": "ควรพิจารณาทำก่อน",
        "score_label": "คะแนนจัดลำดับ",
        "clear": "ล้างรายการทั้งหมด",
        "empty_title": "ยังไม่มีงานในรายการ",
        "empty_caption": "เริ่มเพิ่มงานแรกของคุณได้จากแบบฟอร์มนี้",
        "formula": "คะแนนประเมินจากความเร่งด่วน 40% และความสำคัญ 60%",
        "storage": "รายการจะถูกเก็บไว้ชั่วคราวในเซสชันนี้",
    },
    "en": {
        "language": "Language",
        "theme": "Color",
        "hero_title": "Make your priorities clear<br>and focus on what matters",
        "hero_subtitle": "A calm workspace to plan deadlines and decide what to work on next.",
        "add_title": "Add a task",
        "add_caption": "Add a few details and let Taskflow sort your priorities.",
        "task_name": "Task name",
        "task_placeholder": "e.g. Prepare presentation slides",
        "deadline": "Due in how many days?",
        "deadline_help": "Choose a whole number from 0 to 365 days (0 means due today).",
        "importance": "Importance (1–5)",
        "importance_help": "Rate the impact of the task, not its urgency.",
        "importance_level": ["Very low", "Low", "Moderate", "High", "Critical"],
        "importance_examples": [
            "Optional task to do when time allows",
            "Useful, but can be postponed",
            "Supports a key goal or responsibility",
            "Important outcome or someone is waiting",
            "High impact; should be addressed first",
        ],
        "all_levels": "View importance guide",
        "add_button": "Add task to list",
        "added": "Task added to your list.",
        "empty_name": "Please enter a task name first.",
        "overview": "Your task overview",
        "overview_caption": "Keep priorities and upcoming deadlines in view.",
        "total": "Total tasks",
        "top_score": "Top score",
        "nearest": "Next deadline",
        "day_unit": "days",
        "rank": "Rank",
        "importance_short": "Importance",
        "due_in": "Due in {days} days",
        "urgent": "Consider working on this first",
        "score_label": "Priority score",
        "clear": "Clear all tasks",
        "empty_title": "No tasks yet",
        "empty_caption": "Add your first task using the form.",
        "formula": "Priority score balances urgency (40%) and importance (60%).",
        "storage": "Tasks are stored temporarily for this session.",
    },
    "ja": {
        "language": "言語",
        "theme": "カラー",
        "hero_title": "優先順位を整理して<br>大切なことから始めよう",
        "hero_subtitle": "締め切りを管理し、次に取り組むタスクを見つけるシンプルなワークスペース。",
        "add_title": "タスクを追加",
        "add_caption": "詳細を入力すると、Taskflow が優先順位を整理します。",
        "task_name": "タスク名",
        "task_placeholder": "例：プレゼン資料を準備",
        "deadline": "締め切りまでの日数",
        "deadline_help": "0〜365日の整数を選択してください（0は今日が締め切りです）。",
        "importance": "重要度（1〜5）",
        "importance_help": "緊急度ではなく、タスクの影響度を評価してください。",
        "importance_level": ["とても低い", "低い", "普通", "高い", "最重要"],
        "importance_examples": [
            "時間があるときに行う任意のタスク",
            "役立つが、延期できる",
            "主要な目標や役割に関係する",
            "成果に重要、または誰かが待っている",
            "影響が大きく、優先して対応すべき",
        ],
        "all_levels": "重要度の目安を見る",
        "add_button": "タスクを追加",
        "added": "タスクを追加しました。",
        "empty_name": "タスク名を入力してください。",
        "overview": "タスクの概要",
        "overview_caption": "優先事項と締め切りをひと目で確認できます。",
        "total": "タスク数",
        "top_score": "最高スコア",
        "nearest": "最も近い締め切り",
        "day_unit": "日",
        "rank": "順位",
        "importance_short": "重要度",
        "due_in": "締め切りまであと {days} 日",
        "urgent": "優先して取り組みましょう",
        "score_label": "優先度スコア",
        "clear": "すべて削除",
        "empty_title": "タスクはまだありません",
        "empty_caption": "フォームから最初のタスクを追加してください。",
        "formula": "優先度は緊急度40%、重要度60%で算出します。",
        "storage": "タスクはこのセッション中のみ保存されます。",
    },
}

if "tasks_list" not in st.session_state:
    st.session_state.tasks_list = []
if "app_language" not in st.session_state:
    st.session_state.app_language = "ไทย"
if "app_theme" not in st.session_state:
    st.session_state.app_theme = "Indigo"

top_bar = st.columns([3.5, 1, 1])
with top_bar[0]:
    st.markdown(
        '<div class="brand"><span class="brand-mark">T</span>'
        '<span class="brand-name">taskflow</span>'
        '<span class="brand-divider"></span><span class="brand-note">PERSONAL WORKSPACE</span></div>',
        unsafe_allow_html=True,
    )
with top_bar[1]:
    selected_language = st.selectbox(
        TEXT[LANGUAGES[st.session_state.app_language]]["language"],
        options=list(LANGUAGES),
        key="app_language",
        label_visibility="collapsed",
    )
with top_bar[2]:
    language_code = LANGUAGES[selected_language]
    theme_options = list(THEMES)
    selected_theme = st.selectbox(
        TEXT[language_code]["theme"],
        options=theme_options,
        key="app_theme",
        label_visibility="collapsed",
    )

language_code = LANGUAGES[selected_language]
copy = TEXT[language_code]
palette = THEMES[selected_theme]

st.markdown(
    f"""
    <style>
    :root {{
        --accent: {palette["accent"]};
        --accent-dark: {palette["accent_dark"]};
        --accent-soft: {palette["soft"]};
        --glow: {palette["glow"]};
        --page: {palette["background"]};
        --ink: {palette["ink"]};
        --muted: {palette["muted"]};
        --line: {palette["line"]};
        --card: {palette["card"]};
    }}
    body header[data-testid="stHeader"] {{
        display: none !important;
        height: 0 !important;
    }}
    body [data-testid="stToolbar"], body [data-testid="stAppDeployButton"],
    body [data-testid="stMainMenu"], body [data-testid="stDecoration"], body footer {{
        display: none !important;
    }}
    .stApp {{
        background:
            radial-gradient(ellipse at 8% 0%, var(--glow), transparent 34%),
            linear-gradient(180deg, var(--page) 0%, color-mix(in srgb, var(--page), white 35%) 100%);
        color: var(--ink);
        font-family: Inter, "Noto Sans Thai", "Yu Gothic", Meiryo, sans-serif;
    }}
    .block-container {{
        max-width: 1180px;
        padding-top: 4.2rem;
        padding-bottom: 2.4rem;
    }}
    h1, h2, h3, p, label, [data-testid="stMetricValue"] {{
        font-family: Inter, "Noto Sans Thai", "Yu Gothic", Meiryo, sans-serif;
    }}
    .brand {{
        display: flex;
        align-items: center;
        gap: .65rem;
        min-height: 2.7rem;
    }}
    .brand-mark {{
        display: grid;
        place-items: center;
        width: 2rem;
        height: 2rem;
        border-radius: .7rem;
        color: white;
        background: linear-gradient(145deg, var(--accent), var(--accent-dark));
        font-weight: 700;
        box-shadow: 0 5px 12px var(--glow);
    }}
    .brand-name {{ color: var(--ink); font-size: 1.08rem; font-weight: 700; }}
    .brand-divider {{ height: 1.2rem; border-left: 1px solid var(--line); margin: 0 .1rem; }}
    .brand-note {{ color: var(--muted); font-size: .68rem; letter-spacing: .12em; }}
    div[data-testid="stSelectbox"] {{ margin-top: .12rem; }}
    div[data-testid="stSelectbox"] > div > div {{
        border-radius: 10px;
        border-color: var(--line);
        background: var(--card);
    }}
    .hero {{
        position: relative;
        overflow: hidden;
        padding: 2rem 2.2rem;
        border: 1px solid var(--line);
        border-radius: 22px;
        background: linear-gradient(115deg, var(--card), var(--accent-soft));
        box-shadow: 0 12px 32px rgba(32, 43, 66, .045);
        margin: .5rem 0 1.7rem;
    }}
    .hero:after {{
        content: "";
        position: absolute;
        width: 13rem;
        height: 13rem;
        right: -3.2rem;
        top: -5.8rem;
        border: 1px solid color-mix(in srgb, var(--accent), transparent 78%);
        border-radius: 50%;
        box-shadow: 0 0 0 1.5rem color-mix(in srgb, var(--accent), transparent 93%),
                    0 0 0 3rem color-mix(in srgb, var(--accent), transparent 96%);
        pointer-events: none;
    }}
    .eyebrow {{
        color: var(--accent);
        font-size: .72rem;
        font-weight: 700;
        letter-spacing: .15em;
        margin-bottom: .65rem;
    }}
    .hero h1 {{
        color: var(--ink);
        font-size: clamp(1.8rem, 3vw, 2.55rem);
        line-height: 1.24;
        margin: 0 0 .55rem;
        letter-spacing: -.035em;
    }}
    .hero p {{ color: var(--muted); font-size: .98rem; margin: 0; }}
    .section-heading {{ color: var(--ink); font-size: 1.16rem; font-weight: 700; margin: .2rem 0 .15rem; }}
    .section-caption {{ color: var(--muted); font-size: .88rem; margin: 0 0 1rem; }}
    .level-card {{
        background: var(--accent-soft);
        border: 1px solid color-mix(in srgb, var(--accent), transparent 82%);
        border-radius: 12px;
        padding: .8rem 1rem;
        margin: .2rem 0 1rem;
        color: var(--accent-dark);
    }}
    .level-card strong {{ display: block; margin-bottom: .2rem; }}
    .level-card span {{ font-size: .88rem; opacity: .84; }}
    .task-rank {{ color: var(--accent); font-size: .73rem; font-weight: 700; letter-spacing: .06em; }}
    .score {{ color: var(--accent); font-size: 1.05rem; font-weight: 700; text-align: right; }}
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: var(--card);
        border-color: var(--line);
        border-radius: 15px;
        transition: border-color .2s ease, box-shadow .2s ease, transform .2s ease;
    }}
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
        border-color: color-mix(in srgb, var(--accent), white 60%);
        box-shadow: 0 8px 20px var(--glow);
        transform: translateY(-1px);
    }}
    div[data-testid="stMetric"] {{
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: .75rem 1rem;
    }}
    div[data-testid="stMetricLabel"] {{ color: var(--muted); }}
    div[data-testid="stButton"] > button {{
        border-radius: 10px;
        font-weight: 600;
        min-height: 2.65rem;
        transition: transform .18s ease, box-shadow .18s ease;
    }}
    div[data-testid="stButton"] > button:hover {{ transform: translateY(-1px); }}
    div[data-testid="stButton"] > button[kind="primary"] {{
        background: var(--accent);
        border-color: var(--accent);
    }}
    div[data-testid="stButton"] > button[kind="primary"]:hover {{
        background: var(--accent-dark);
        border-color: var(--accent-dark);
        box-shadow: 0 5px 14px var(--glow);
    }}
    div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {{
        border-radius: 10px;
        background: var(--card);
    }}
    div[data-testid="stProgress"] > div > div > div {{ background: var(--accent); }}
    .footnote {{
        color: var(--muted);
        font-size: .8rem;
        border-top: 1px solid var(--line);
        margin-top: 1.4rem;
        padding-top: .9rem;
    }}
    @media (max-width: 700px) {{
        .block-container {{ padding-top: .8rem; }}
        .brand-note, .brand-divider {{ display: none; }}
        .hero {{ padding: 1.5rem; border-radius: 17px; }}
    }}
    </style>
    <header class="hero">
      <div class="eyebrow">TASKFLOW &nbsp; / &nbsp; PERSONAL WORKSPACE</div>
      <h1>{copy["hero_title"]}</h1>
      <p>{copy["hero_subtitle"]}</p>
    </header>
    """,
    unsafe_allow_html=True,
)

if "tasks_list" not in st.session_state:
    st.session_state.tasks_list = []

entry_column, queue_column = st.columns([0.9, 1.1], gap="large")

with entry_column:
    st.markdown(f'<div class="section-heading">{copy["add_title"]}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<p class="section-caption">{copy["add_caption"]}</p>',
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        task_title = st.text_input(copy["task_name"], placeholder=copy["task_placeholder"])
        deadline = st.slider(
            copy["deadline"],
            min_value=0,
            max_value=365,
            value=1,
            step=1,
            help=copy["deadline_help"],
        )
        importance_level = st.slider(
            copy["importance"],
            min_value=1,
            max_value=5,
            value=3,
            help=copy["importance_help"],
        )
        importance_name = copy["importance_level"][importance_level - 1]
        importance_example = copy["importance_examples"][importance_level - 1]
        st.markdown(
            f'<div class="level-card"><strong>{copy["importance"]}: '
            f'{importance_level} · {importance_name}</strong>'
            f"<span>{importance_example}</span></div>",
            unsafe_allow_html=True,
        )
        with st.expander(copy["all_levels"]):
            for level, (name, example) in enumerate(
                zip(copy["importance_level"], copy["importance_examples"]),
                start=1,
            ):
                st.write(f"**{level} — {name}:** {example}")

        if st.button(copy["add_button"], type="primary", use_container_width=True):
            if task_title.strip():
                whole_days = int(deadline)
                urgency_score = 10 / max(whole_days, 0.5)
                priority_score = (urgency_score * 0.4) + (importance_level * 0.6)
                st.session_state.tasks_list.append(
                    {
                        "title": task_title.strip(),
                        "deadline": whole_days,
                        "importance": importance_level,
                        "score": round(priority_score, 2),
                    }
                )
                st.success(copy["added"])
            else:
                st.warning(copy["empty_name"])

with queue_column:
    st.markdown(f'<div class="section-heading">{copy["overview"]}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<p class="section-caption">{copy["overview_caption"]}</p>',
        unsafe_allow_html=True,
    )

    if st.session_state.tasks_list:
        sorted_tasks = sorted(
            st.session_state.tasks_list,
            key=lambda task: task["score"],
            reverse=True,
        )
        top_task = sorted_tasks[0]
        metric_columns = st.columns(3)
        metric_columns[0].metric(copy["total"], len(sorted_tasks))
        metric_columns[1].metric(copy["top_score"], top_task["score"])
        nearest_deadline = min(int(task["deadline"]) for task in sorted_tasks)
        metric_columns[2].metric(
            copy["nearest"],
            f'{nearest_deadline} {copy["day_unit"]}',
        )

        for index, task in enumerate(sorted_tasks, 1):
            with st.container(border=True):
                title_column, score_column = st.columns([4, 1])
                with title_column:
                    st.markdown(
                        f'<div class="task-rank">{copy["rank"]} {index} · '
                        f'{copy["importance_short"]} {task["importance"]}</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**{task['title']}**")
                    st.caption(copy["due_in"].format(days=int(task["deadline"])))
                with score_column:
                    st.markdown(
                        f'<div class="score">{task["score"]}</div>',
                        unsafe_allow_html=True,
                    )
                if task["score"] >= 6:
                    st.progress(1.0, text=copy["urgent"])
                else:
                    st.progress(min(task["score"] / 6, 1.0), text=copy["score_label"])

        if st.button(copy["clear"], type="secondary"):
            st.session_state.tasks_list = []
            st.rerun()
    else:
        with st.container(border=True):
            st.markdown(f"**{copy['empty_title']}**")
            st.caption(copy["empty_caption"])

st.markdown(
    f'<div class="footnote">{copy["formula"]} &nbsp; · &nbsp; {copy["storage"]}</div>',
    unsafe_allow_html=True,
)
