import random
import streamlit as st

# إعداد صفحة الموقع وتصميم الثيم الفخم المستوحى من الهوية الوطنية (عزنا بطبعنا)
st.set_page_config(
    page_title="اليوم الوطني السعودي 96 - عزنا بطبعنا",
    page_icon="saudi arabia",
    layout="centered",
)

# تخصيص التصميم المتقدم والاحترافي مع شعار جامعة حائل
st.markdown(
    """
    <style>
    /* إخفاء شريط Streamlit العلوي والسفلي لنظافة الواجهة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: linear-gradient(135deg, #051612 0%, #08241d 50%, #030d0a 100%);
        color: #ffffff;
        font-family: 'Tahoma', sans-serif;
    }

    /* الهيدر الفخم */
    .hero-container {
        background: linear-gradient(145deg, #0b352b 0%, #041813 100%);
        border: 2px solid #d4af37;
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
        position: relative;
        overflow: hidden;
    }
    .hero-container::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 4px;
        background: linear-gradient(90deg, #d4af37, #ffffff, #d4af37);
    }
    .hero-title {
        color: #ffffff;
        font-size: 34px;
        font-weight: 900;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    .hero-badge {
        background: rgba(212, 175, 55, 0.15);
        color: #ffd700;
        padding: 8px 25px;
        border-radius: 30px;
        border: 1px solid #d4af37;
        display: inline-block;
        font-size: 19px;
        font-weight: bold;
        margin-top: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    /* تصميم بطاقات الأسئلة الاحترافية */
    .question-card {
        background: linear-gradient(145deg, #0c382e 0%, #07221b 100%);
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #1a5c4a;
        border-right: 6px solid #d4af37;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    }

    /* تحسين شكل الأزرار والتفاعل معها */
    .stButton>button {
        background: linear-gradient(135deg, #0d382e 0%, #08261e 100%);
        color: #ffffff;
        border: 1px solid #d4af37;
        border-radius: 12px;
        font-size: 17px;
        font-weight: bold;
        width: 100%;
        padding: 14px 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #d4af37 0%, #b3922f 100%);
        color: #051612;
        border: 1px solid #ffffff;
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(212,175,55,0.4);
    }

    /* صندوق النتيجة الكبرى */
    .result-box {
        background: linear-gradient(135deg, #0d382e 0%, #051a14 100%);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #d4af37;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# قاعدة بيانات الأسئلة الحصرية والكاملة (10 أسئلة لكل موضوع)
topics_data = {
    "أسئلة عامة عن اليوم الوطني السعودي": [
        {
            "q": "ما هو الشعار الرسمي المعتمد لليوم الوطني السعودي الـ 96؟",
            "options": ["عزنا بطبعنا", "نحلم ونحقق", "همة حتى القمة", "رؤيتنا تهندس المستقبل"],
            "answer": "عزنا بطبعنا",
        },
        {
            "q": "في أي عام ميلادي تم إعلان توحيد المملكة العربية Saudi Arabia؟",
            "options": ["1932", "1902", "1950", "1920"],
            "answer": "1932",
        },
        {
            "q": "ما هو التاريخ الميلادي الثابت للاحتفال باليوم الوطني كل عام؟",
            "options": ["23 سبتمبر", "1 يناير", "15 أغسطس", "30 نوفمبر"],
            "answer": "23 سبتمبر",
        },
        {
            "q": "من هو الملك الذي أعلن توحيد البلاد تحت اسم 'المملكة العربية Saudi Arabia'؟",
            "options": [
                "الملك عبد العزيز آل سعود",
                "الملك فهد بن عبد العزيز",
                "الملك سعود بن عبد العزيز",
                "الملك فيصل بن عبد العزيز",
            ],
            "answer": "الملك عبد العزيز آل سعود",
        },
        {
            "q": "ماذا يرمز اللون الأخضر في علم المملكة العربية Saudi Arabia؟",
            "options": ["النماء والرخاء والسلام", "البحر والتراب", "الصحراء والقحط", "التجارة والمال"],
            "answer": "النماء والرخاء والسلام",
        },
        {
            "q": "ما هو الشعار الوطني المكتوب بجانب السيفين والنخلة في علم المملكة؟",
            "options": [
                "لا إله إلا الله محمد رسول الله",
                "الله أكبر ولله الحمد",
                "عزنا بطبعنا",
                "نحلم ونحقق",
            ],
            "answer": "لا إله إلا الله محمد رسول الله",
        },
        {
            "q": "كم عدد مناطق الإدارية الرئيسية في المملكة العربية Saudi Arabia؟",
            "options": ["13", "10", "15", "12"],
            "answer": "13",
        },
        {
            "q": "بأمر ملكي، متى أصبح اليوم الوطني إجازة رسمية سنوية للجميع؟",
            "options": ["عام 2005", "عام 1990", "عام 2015", "عام 1950"],
            "answer": "عام 2005",
        },
        {
            "q": "ما هو الرمز الوطني الذي تتوسطه النخلة في شعار الدولة؟",
            "options": ["سيفان متقاطعان", "بندقية عربية", "درع وقوس", "حصان عربي أصيل"],
            "answer": "سيفان متقاطعان",
        },
        {
            "q": "أي من الألوان التالية يُميز هوية اليوم الوطني مع الأخضر الداكن؟",
            "options": [
                "الدرجات التراثية والذهبية",
                "الأحمر الفاقع",
                "الأزرق الفاتح",
                "البرتقالي النيون",
            ],
            "answer": "الدرجات التراثية والذهبية",
        },
    ],
    "مدن المملكة العربية السعودية": [
        {
            "q": "ما هي العاصمة الإدارية والسياسية للمملكة العربية Saudi Arabia؟",
            "options": ["الرياض", "جدة", "مكة المكرمة", "الدمام"],
            "answer": "الرياض",
        },
        {
            "q": "ما هي المدينة التي تُلقب بـ 'عروس البحر الأحمر'؟",
            "options": ["جدة", "ينبع", "الخبر", "أملج"],
            "answer": "جدة",
        },
        {
            "q": "ما هو الاسم الإداري للمنطقة التي تقع فيها مدينة حائل؟",
            "options": ["منطقة حائل", "منطقة القصيم", "منطقة تبوك", "منطقة الجوف"],
            "answer": "منطقة حائل",
        },
        {
            "q": "ما هي المدينة الكبرى التي تشتهر بكونها عاصمة التمور والزراعة في وسط القصيم؟",
            "options": ["بريدة", "عنيزة", "الرس", "المذنب"],
            "answer": "بريدة",
        },
        {
            "q": "أين تقع أضخم واحة نخيل طبيعية في العالم (واحة الأحساء)؟",
            "options": ["المنطقة الشرقية", "منطقة عسير", "منطقة الباحة", "منطقة نجران"],
            "answer": "المنطقة الشرقية",
        },
        {
            "q": "مدينة سياحية جبلية في جنوب المملكة تشتهر بالأجواء الباردة والمنتزهات الخضراء؟",
            "options": ["أبها", "تبوك", "حائل", "الرياض"],
            "answer": "أبها",
        },
        {
            "q": "ما هي المدينة الاقتصادية الكبرى الواقعة على ساحل الخليج العربي بالشرقية؟",
            "options": ["الجبيل", "رابغ", "ينبع", "الدرعية"],
            "answer": "الجبيل",
        },
        {
            "q": "أي من المدن التالية تعتبر وجهة رئيسية لمشروع 'نيوم' المستقبلي؟",
            "options": ["تبوك", "أبها", "الطائف", "جازان"],
            "answer": "تبوك",
        },
        {
            "q": "مدينة تاريخية تقع في أقصى جنوب المملكة وتشتهر بسدودها التاريخية والزراعة؟",
            "options": ["نجران", "الخرج", "حفر الباطن", "عرعر"],
            "answer": "نجران",
        },
        {
            "q": "ما هي أقصى مدينة حدودية في الشمال للمملكة؟",
            "options": ["عرعر", "سكاكا", "القريات", "رفحاء"],
            "answer": "عرعر",
        },
    ],
    "تاريخ وحضارة السعودية": [
        {
            "q": "في أي عام تم تأسيس الدولة السعودية الأولى (إمارة الدرعية)؟",
            "options": ["1727", "1932", "1785", "1688"],
            "answer": "1727",
        },
        {
            "q": "من هو مؤسس الدولة السعودية الأولى؟",
            "options": [
                "الإمام محمد بن سعود",
                "الملك عبد العزيز",
                "الإمام تركي بن عبد الله",
                "الإمام سعود الكبير",
            ],
            "answer": "الإمام محمد بن سعود",
        },
        {
            "q": "ما هو الحي التاريخي الشهير في الدرعية والذي يُعد مسجلاً في اليونسكو؟",
            "options": ["حي الطريف", "حي البجيري", "حي المربع", "حي السفارات"],
            "answer": "حي الطريف",
        },
        {
            "q": "في أي عام تمكن الملك عبد العزيز من استرداد الرياض وتأسيس الدولة السعودية الثالثة؟",
            "options": ["1902", "1932", "1824", "1727"],
            "answer": "1902",
        },
        {
            "q": "ما اسم قصر الحكم التاريخي الشهير في الرياض الذي ارتبط باسترداد المدينة؟",
            "options": ["قصر المصمك", "قصر المربع", "قصر شقراء", "قصر شبرا"],
            "answer": "قصر المصمك",
        },
        {
            "q": "ما هو اسم الدولة السعودية الثانية التي أسسها الإمام تركي بن عبد الله؟",
            "options": ["إمارة نجد", "سلطنة الحجاز", "مملكة الحجاز ونجد", "إمارة الدرعية"],
            "answer": "إمارة نجد",
        },
        {
            "q": "ما هي النقوش والرسوم الأثرية الشهيرة المكتشفة في حائل (جبة وشهبة)؟",
            "options": [
                "نقوش ورسوم ثمودية وبشرية وحيوانية قديمة",
                "كتابات باللغة اللاتينية الحديثة",
                "رسوم فرعونية قديمة",
                "خطوط فارسية حديثة",
            ],
            "answer": "نقوش ورسوم ثمودية وبشرية وحيوانية قديمة",
        },
        {
            "q": "ما هو الطريق التجاري التاريخي العريق الذي كان يربط جنوب الجزيرة بالشمال وقوافل البخور؟",
            "options": [
                "طريق البخور التاريخي",
                "طريق الحرير البحري",
                "طريق التوابل الأوروبي",
                "طريق القوافل الصحراوية الحديثة",
            ],
            "answer": "طريق البخور التاريخي",
        },
        {
            "q": "متى تم توحيد اسم الدولة رسمياً إلى 'المملكة العربية Saudi Arabia'؟",
            "options": ["1932", "1902", "1926", "1950"],
            "answer": "1932",
        },
        {
            "q": "ما هو الاسم التاريخي لمدينة الرياض قديماً قبل أن تحمل اسمها الحالي؟",
            "options": ["حجر اليمامة", "يثرب", "الطائف", "أوبار"],
            "answer": "حجر اليمامة",
        },
    ],
    "مدن السعودية": [
        {
            "q": "ما هي المدينة التاريخية التي تضم موقع 'مدائن صالح' (الحجر) الأثري؟",
            "options": ["العلا", "تبوك", "حائل", "المدينة المنورة"],
            "answer": "العلا",
        },
        {
            "q": "ما هو الجبلين الشهيرين اللذين يقترنان بذكر مدينة حائل دائماً في الشعر والموروث؟",
            "options": ["أجا وسلمى", "أحد وثبير", "طويق وجبل قانون", "السروات ولبن"],
            "answer": "أجا وسلمى",
        },
        {
            "q": "ما هي المدينة الملقبة بـ 'بوابة الحرمين الشريفين' الكبرى للقادمين بحراً وجواً؟",
            "options": ["جدة", "الرياض", "الدمام", "الجبيل"],
            "answer": "جدة",
        },
        {
            "q": "مدينة تشتهر بزراعة الورود والزهور وتقع فوق جبال السروات المرتفعة؟",
            "options": ["الطائف", "بريدة", "جازان", "الخرمة"],
            "answer": "الطائف",
        },
        {
            "q": "محافظة ينبع الصناعية والتاريخية تقع على الساحل الشرقي لأي بحر؟",
            "options": ["البحر الأحمر", "الخليج العربي", "بحر العرب", "بحر قزوين"],
            "answer": "البحر الأحمر",
        },
        {
            "q": "ما هي عاصمة منطقة القصيم التي تُعد مركزاً تجارياً واقتصادياً ضخماً؟",
            "options": ["بريدة", "عنيزة", "الرس", "البكيرية"],
            "answer": "بريدة",
        },
        {
            "q": "مدينة حدودية شمالية غربية تتميز بمشروع نيوم ومقومات السياحة الساحلية الواعدة؟",
            "options": ["تبوك", "عرعر", "سكاكا", "رفحاء"],
            "answer": "تبوك",
        },
        {
            "q": "مدينة سعودية كبرى على الخليج العربي تُعتبر العاصمة الإدارية للمنطقة الشرقية؟",
            "options": ["الدمام", "الخبر", "القطيف", "الظهران"],
            "answer": "الدمام",
        },
        {
            "q": "مدينة في الجنوب الغربي تتميز بالزراعة المدرجية ومنتزه السودة السياحي؟",
            "options": ["أبها", "نجران", "جازان", "الباحة"],
            "answer": "أبها",
        },
        {
            "q": "ما هي الواحة الشهيرة بالمنطقة الشرقية التي تضم عيون الماء التاريخية والنخيل؟",
            "options": ["الأحساء", "القطيف", "بقيق", "الخفجي"],
            "answer": "الأحساء",
        },
    ],
    "ثقافة المملكة العربية السعودية": [
        {
            "q": "ما هي الرقصة الشعبية الرسمية الأولى في المملكة التي تُؤدى بالسيف والتدققات؟",
            "options": [
                "العرضة السعودية",
                "السامري",
                "الدحّة",
                "المزكاة أو الخبيتي",
            ],
            "answer": "العرضة السعودية",
        },
        {
            "q": "ما هو اللباس التقليدي الأصيل للرجل السعودي في المناسبات الوطنية واليوم الوطني؟",
            "options": [
                "الثوب والشماغ (أو الغترة)",
                "البشت والعمامة فقط",
                "الملابس الغربية الرسمية",
                "العباءة والملابس الرياضية",
            ],
            "answer": "الثوب والشماغ (أو الغترة)",
        },
        {
            "q": "ما هي المشروبات التقليدية التي تُعد رمزاً أصيلاً للكرم والضيافة السعودية؟",
            "options": [
                "القهوة السعودية (بالهيل والقرنفل)",
                "القهوة الفرنسية",
                "الشاي الأسود الثقيل فقط",
                "عصير الفواكه الطازجة",
            ],
            "answer": "القهوة السعودية (بالهيل والقرنفل)",
        },
        {
            "q": "ما هو الرفيق الأساسي والدائم للقهوة السعودية في الضيافة التقليدية؟",
            "options": ["التمر", "الشوكولاتة المستوردة", "المكسرات المالحة", "المعجنات الغربية"],
            "answer": "التمر",
        },
        {
            "q": "ما هو اسم الفن والهندسة التقليدية لتزيين الجدران الداخلية للمنازل (خاصة في عسير)؟",
            "options": [
                "فن القط العسيري",
                "النقش الفرعوني",
                "الزخرفة الباروكية",
                "الفن الروماني القديم",
            ],
            "answer": "فن القط العسيري",
        },
        {
            "q": "ما هي مكانة الصقور والصقارة في الثقافة والتراث السعودي الأصيل؟",
            "options": [
                "موروث عريق ورمز للصبر والفروسية والصيد",
                "مجرد طيور عادية للزينة الحديثة",
                "ليست ذات اهتمام ثقافي",
                "حيوانات أليفة في المنازل فقط",
            ],
            "answer": "موروث عريق ورمز للصبر والفروسية والصيد",
        },
        {
            "q": "ما هو اسم المجلس التقليدي في الثقافة السعودية المسجل في قائمة اليونسكو للتراث غير المادي؟",
            "options": [
                "المجلس (مكان الاستقبال والتشاور)",
                "الديوانية الحديثة",
                "الصالون التجاري المغلق",
                "المقهى الشعبي",
            ],
            "answer": "المجلس (مكان الاستقبال والتشاور)",
        },
        {
            "q": "ما هو الفن الشعبي التراثي المرتبط بالشعر والغناء الجماعي باستخدام الدفوف في نجد؟",
            "options": ["السامري", "الراب", "الجاز", "البلوز"],
            "answer": "السامري",
        },
        {
            "q": "ما هو السيف العربي التقليدي وأهميته الرمزية في الثقافة السعودية؟",
            "options": [
                "رمز للشجاعة والقوة والعزة والاحتفال الرسمي",
                "أداة مطبخية قديمة",
                "سلاح حربي عشوائي للاستخدام اليومي",
                "قطعة ديكور غربية",
            ],
            "answer": "رمز للشجاعة والقوة والعزة والاحتفال الرسمي",
        },
        {
            "q": "ما هو الفن الشعبي الشهير الذي تشتهر به مناطق شمال المملكة (مثل تبوك والجوف) ويعتمد على صف الصفوف وإصدار أصوات حماسية؟",
            "options": ["الدحّة", "العرضة العسيرية", "الخبيتي", "الينبعاوي"],
            "answer": "الدحّة",
        },
    ],
}

# تهيئة الحالات في الذاكرة (Session State)
if "page" not in st.session_state:
    st.session_state.page = "home"
if "current_topic" not in st.session_state:
    st.session_state.current_topic = None
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = []
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "shuffled_options_cache" not in st.session_state:
    st.session_state.shuffled_options_cache = {}

# --- الصفحة الرئيسية ---
if st.session_state.page == "home":
    # عرض شعار جامعة حائل أعلى الهيدر (مشروع جامعي)
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 10px;">
            <span style="background-color: #0b352b; color: #d4af37; padding: 6px 18px; border-radius: 15px; border: 1px solid #d4af37; font-weight: bold; font-size: 15px;">
                🎓 University of Hail — مشروع اليوم الوطني 96
            </span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-container">
            <h1 class="hero-title">🇸🇦 اليوم الوطني السعودي 96 🇸🇦</h1>
            <div class="hero-badge">عِزُّنا بطبِعنا</div>
            <p style="font-size: 17px; color: #cfdcd6; margin-top: 15px; line-height: 1.6;">
                منصة تفاعلية وطنية لاختبار المعلومات عبر أقسام متنوعة.<br>اختر أحد المواضيع أدناه وابدأ التحدي الآن!
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h3 style='text-align: center; color: #d4af37; margin-bottom: 20px;'>✨ قــائمــة الأســـئلة ✨</h3>",
        unsafe_allow_html=True,
    )

    topics_list = list(topics_data.keys())
    for i, topic in enumerate(topics_list, 1):
        if st.button(
            f"الموضوع ({i}) ⟵  {topic}", key=f"topic_btn_{i}", use_container_width=True
        ):
            st.session_state.current_topic = topic

            # خلط الأسئلة عشوائياً لكل مستخدم وكل دخول
            q_list = topics_data[topic].copy()
            random.shuffle(q_list)
            st.session_state.shuffled_questions = q_list

            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.shuffled_options_cache = {}
            st.session_state.page = "quiz"
            st.rerun()

# --- صفحة الأسئلة ---
elif st.session_state.page == "quiz":
    topic = st.session_state.current_topic
    q_list = st.session_state.shuffled_questions
    idx = st.session_state.q_index
    total_q = len(q_list)

    # شريط التقدم البصري الفخم
    st.progress((idx + 1) / total_q)

    st.markdown(
        f"""
        <div style="background: rgba(13, 56, 46, 0.7); padding: 12px; border-radius: 12px; border: 1px solid #d4af37; text-align: center; margin-bottom: 20px;">
            <span style="color: #d4af37; font-weight: bold; font-size: 18px;">{topic}</span>
            <span style="float: left; color: #a3c1ad; font-size: 15px;">السؤال {idx + 1} من {total_q}</span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    current_q = q_list[idx]

    st.markdown(
        f"""
        <div class="question-card">
            <h3 style="color: #ffffff; line-height: 1.6; margin: 0; font-size: 20px;">{current_q['q']}</h3>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # خلط الخيارات عشوائياً وتخزينها لثباتها أثناء الاختيار
    if idx not in st.session_state.shuffled_options_cache:
        opts = current_q["options"].copy()
        random.shuffle(opts)
        st.session_state.shuffled_options_cache[idx] = opts

    shuffled_opts = st.session_state.shuffled_options_cache[idx]

    selected_choice = st.radio(
        "اختر الإجابة المناسبة:", shuffled_opts, key=f"q_choice_{idx}"
    )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("التالي ⬅️", use_container_width=True):
            if selected_choice == current_q["answer"]:
                st.session_state.score += 1

            if idx + 1 < total_q:
                st.session_state.q_index += 1
                st.rerun()
            else:
                st.session_state.page = "result"
                st.rerun()

    with col2:
        if st.button("🏠 الرئيسية", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

# --- صفحة النتيجة ---
elif st.session_state.page == "result":
    score = st.session_state.score
    total = len(st.session_state.shuffled_questions)

    st.markdown(
        f"""
        <div class="result-box">
            <h1 style="color: #d4af37; margin-bottom: 10px;">نتيجتك النهائية</h1>
            <div class="hero-badge" style="margin-bottom: 20px;">عِزُّنا بطبِعنا</div>
            <h2 style="color: #ffffff; font-size: 32px; margin-top: 15px;">
                حققت <span style="color: #ffd700; font-size: 45px;">{score}</span> من <span style="color: #ffd700; font-size: 45px;">{total}</span>
            </h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # إذا جاب الدرجة الكاملة (10/10)
    if score == total:
        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #134e3e 0%, #061c16 100%); padding: 30px; border-radius: 15px; text-align: center; border: 2px solid #ffd700; margin-top: 25px; box-shadow: 0 8px 25px rgba(212,175,55,0.3);">
                <h2 style="color: #ffd700; margin-bottom: 12px;">🎉 مبروك مليون! إنجاز وطني مشرف! 🎉</h2>
                <p style="font-size: 20px; color: #ffffff; line-height: 1.7;">
                    أبدعت وحصلت على الدرجة الكاملة بجدارة فائقة!<br>
                    <b>عِزُّنا بطبِعنا</b> ومعلوماتك الوطنية مصدر فخر واعتزاز.
                </p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.balloons()
    else:
        st.markdown(
            """
            <div style="background: rgba(12, 56, 46, 0.5); padding: 22px; border_radius: 15px; text-align: center; margin-top: 25px; border: 1px solid #1a5c4a;">
                <p style="font-size: 18px; color: #dcdcdc; margin: 0;">مشاركة متميزة جداً! استمر في الاختبار وحاول مرة أخرى لتحقيق الدرجة الكاملة.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 إعادة المحاولة", use_container_width=True):
            q_list = topics_data[st.session_state.current_topic].copy()
            random.shuffle(q_list)
            st.session_state.shuffled_questions = q_list
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.shuffled_options_cache = {}
            st.session_state.page = "quiz"
            st.rerun()

    with col2:
        if st.button("🏠 العودة للرئيسية", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()