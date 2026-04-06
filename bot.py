from typing import Final
import os
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, ApplicationBuilder, ConversationHandler



TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = '@AP_Digital_bot'
GROUP_USERNAME: Final = '@APDigitalSD'



# Commands
MAIN_MENU = 0
STARLINK_MENU = 1
STARLINK_SUBMENU = 5
USDT_MENU  = 2
BUY_USDT_SUBMENU = 3
SELL_USDT_SUBMENU = 4
MBOKAED_MENU = 6
MBOKRWF_MENU = 7
GET_AMOUNT_BUY = 8
GET_AMOUNT_SELL = 9
GET_AMOUNT_MBOK_AED = 10
GET_AMOUNT_MBOK_RWF = 11


CB_STARLINK = 'starlink'
CB_BACK_STARLINK_COUNTRIES = 'back_to_starlink_countries'
CB_USDT = 'USDT'
CB_MBOK_AED = 'mbok_aed'
CB_MBOK_RWF = 'mbok_rwf'
CB_SELL = 'SELL_USDT'
CB_BUY = 'BUY_USDT'

#للعايز يشتري 

SDG_TO_USDT:float = 3630
SDG_TO_USDT:float = 4200
AED_TO_USDT:float = 3.75
RWF_TO_USDT:float = 1480

#للعايز يبيع
USDT_TO_SDG:float = 3900
USDT_TO_AED:float = 3.6
USDT_TO_RWF:float = 1445
USDT_TO_RWF:float = 1430

# User pays AED, receives SDG
SDG_TO_AED:float = 1145
CB_MBOK_SDG_AED = 'mbok_aed_sdg_flow'

# User pays SDG, receives AED
AED_TO_SDG_LESS:float = 950.00
AED_TO_SDG_MORE:float = 1050.00
CB_MBOK_AED_SDG = 'mbok_sdg_aed_flow'


 # User pays RWF, receives SDG
RWF_TO_SDG:float = 1/38*100
CB_MBOK_RWF_SDG = 'mbok_rwf_sdg_flow'

 # User pays RWF, receives SDG
CB_MBOK_SDG_RWF = 'mbok_sdg_rwf_flow'
SDG_TO_RWF:float = 41/100


CB_AED = 'AED'
tele_user = url = "https://t.me/APDigitalStores"
ARGENTINA_LINK = url = "https://wa.me/p/32578787798431918/249120095551"
RWANDA_LINK = url = "https://wa.me/p/25149003804712308/249120095551"
PHILIPPINES_LINK = url = "https://wa.me/p/25877716681815156/249120095551"
ZAMBIA_LINK = url = "https://wa.me/p/32202032589442635/249120095551"
KENYA_LINK = url = "https://wa.me/p/24623819307319199/249120095551"
HAITI_LINK = url = "https://wa.me/p/24707781225587721/249120095551"
MALAWI_LINK = url = "https://wa.me/p/25519788000979166/249120095551"
EUROPE_LINK = url = "https://wa.me/p/24303998762608973/249120095551"
YEMEN_LINK = url = "https://wa.me/p/24977806058545878/249120095551"
MOZAMBIQUE_LINK = url = "https://wa.me/p/25439013535732866/249120095551"
PERU_LINK = url   =    "https://wa.me/p/32613727734907924/249120095551"
USDT_AED_LINK = url = "https://wa.me/p/25957522323836834/249120095551"
USDT_SDG_LINK = url = "https://wa.me/p/24957747800562016/249120095551"
USDT_RWF_LINK = url = "https://wa.me/qr/JMWGFE55VVLFK1"
GRUOP_LINk   = url = "https://t.me/APDigitalSD"

CB_SDG = 'SDG'
CB_RWF = 'RWF'
CB_BACK_USDT = 'back_to_usdt'
CB_AED_BACK_TO_MENU = 'back_to_menu_aed'
CB_RWF_BACK_TO_MENU = 'back_to_menu_rwf'

CB_ARGENTINA = 'argentina_starlink'
CB_RWANDA = 'rwanda_starlink'
CB_THE_PHILIPPINES = 'the_philippines_starlink'
CB_MALAWI = 'malawi_starlink'
CB_KENYA = 'kenya_starlink'
CB_HAITI = 'haiti_starlink'
CB_MOZAMBIQUE = 'mozambique_starlink'
CB_PERU = 'peru_starlink'
CB_ZAMBIA = 'zambia_starlink'
CB_YEMEN = 'yemen_starlink'
CB_EUROPE = 'europe_starlink'
CB_BACK = 'back_to_main'

async def check_membership(context: ContextTypes.DEFAULT_TYPE, user_id: int, group_id: str) -> bool:
    
    try:
        member = await context.bot.get_chat_member(group_id, user_id)
        
        return member.status in ['creator', 'administrator', 'member']
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE)->int:
    user = update.effective_user
    user_first_name = user.first_name
    
    is_member = await check_membership(context, user.id, GROUP_USERNAME)
    if not is_member:
        join_link = GRUOP_LINk
        
        keyboard = [
            [InlineKeyboardButton("اضغط هنا للانضمام إلى المجموعة 🔗", url = join_link)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        message_text = f"""
{user_first_name}، أهلاً بك في 🌟 AP Digital Store 🌟

للاستفادة من خدماتنا، **يجب عليك الانضمام إلى مجموعتنا أولاً**. 
يرجى الانضمام والضغط على /start مرة أخرى.
"""
        if update.callback_query:
            await update.callback_query.answer()
            await update.callback_query.edit_message_text(
                text= message_text,
                reply_markup=reply_markup
            )
        else:
            await update.message.reply_text(
                text=message_text,
                reply_markup=reply_markup
            )
        return MAIN_MENU

    keyboard = [
        [InlineKeyboardButton("Starlink | ستارلينك ", callback_data=CB_STARLINK)],
        [InlineKeyboardButton("USDT | دولار رقمي", callback_data=CB_USDT)],
        [InlineKeyboardButton("بنكك 💱 درهم", callback_data=CB_MBOK_AED)],
        [InlineKeyboardButton("بنكك 💱 فرانك رواندي", callback_data=CB_MBOK_RWF)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text=f"""{user_first_name} حبابك \n 🌟 AP Digital Store 🌟
أهلاً بكم في عالم الخدمات الرقمية

🔹 نقدم لكم خدماتنا باحترافية ومصداقية، لنكون دائماً وجهتكم الأولى في عالم الحلول الرقمية:

✨ بيع وشراء العملات الرقمية
نُسهِّل عليك تحويل أموالك بين الجنيه السوداني، الدرهم الإماراتي، الدولار، اليورو وأيضاً الفرنك الرواندي بأفضل الأسعار.

💱 تحويل الجنيه السوداني إلى الفرنك الرواندي 🇸🇩💱🇷🇼
خدمة جديدة تتيح لك التحويل بسهولة وأمان عبر مسار موثوق: جنيه سوداني → فرنك رواندي.

🚀 تفعيل وتجديد أجهزة ستارلينك
خدمة سريعة وفعالة لتبقى متصلاً دائماً بالإنترنت الفضائي.

🎁 بطاقات الهدايا (Gift Cards)
نوفر لك مجموعة متنوعة من بطاقات الهدايا لتلبية احتياجاتك.

💳 الدفع الإلكتروني للمواقع
نؤمن عمليات الدفع بكل أمان وسلاسة لمختلف المنصات والمواقع.

📞 خدمتكم شرف لنا!
تواصلوا معنا الآن واستمتعوا بتجربة فريدة من نوعها.
            
            
             """,
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            f"""{user_first_name} حبابك \n 🌟 AP Digital Store 🌟
أهلاً بكم في عالم الخدمات الرقمية

🔹 نقدم لكم خدماتنا باحترافية ومصداقية، لنكون دائماً وجهتكم الأولى في عالم الحلول الرقمية:

✨ بيع وشراء العملات الرقمية
نُسهِّل عليك تحويل أموالك بين الجنيه السوداني، الدرهم الإماراتي، الدولار، اليورو وأيضاً الفرنك الرواندي بأفضل الأسعار.

💱 تحويل الجنيه السوداني إلى الفرنك الرواندي 🇸🇩💱🇷🇼
خدمة جديدة تتيح لك التحويل بسهولة وأمان عبر مسار موثوق: جنيه سوداني → فرنك رواندي.

🚀 تفعيل وتجديد أجهزة ستارلينك
خدمة سريعة وفعالة لتبقى متصلاً دائماً بالإنترنت الفضائي.

🎁 بطاقات الهدايا (Gift Cards)
نوفر لك مجموعة متنوعة من بطاقات الهدايا لتلبية احتياجاتك.

💳 الدفع الإلكتروني للمواقع
نؤمن عمليات الدفع بكل أمان وسلاسة لمختلف المنصات والمواقع.

📞 خدمتكم شرف لنا!
تواصلوا معنا الآن واستمتعوا بتجربة فريدة من نوعها.
            
            
             """,
            reply_markup=reply_markup
        )
    return MAIN_MENU

async def starlink_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Sends the Starlink country sub-menu."""
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("الارجنتين 🇦🇷 | 87,500 ARS", callback_data=CB_ARGENTINA)],
        [InlineKeyboardButton("🇪🇺  أوروبا | 89 €", callback_data=CB_EUROPE)],
        [InlineKeyboardButton("🇭🇹 هايتي | 85$", callback_data=CB_HAITI)],
        [InlineKeyboardButton("KES 14,000 | 🇰🇪 كينيا", callback_data=CB_KENYA)],
        [InlineKeyboardButton("MWK 170,000 |🇲🇼 ملاوي", callback_data=CB_MALAWI)],
        [InlineKeyboardButton("MZN 6,000 | 🇲🇿 موزمبيق",callback_data=CB_MOZAMBIQUE)],
        [InlineKeyboardButton("PEN 335 | 🇵🇪 بيرو", callback_data=CB_PERU)],
        [InlineKeyboardButton("RWF 128,000 | 🇷🇼 رواندا", callback_data=CB_RWANDA)],
        [InlineKeyboardButton("🇵🇭 الفلبين | 5,700₱", callback_data=CB_THE_PHILIPPINES)],
        [InlineKeyboardButton("🇾🇪  اليمن | 100 $" , callback_data=CB_YEMEN)],
        [InlineKeyboardButton("ZMW 2,500 | 🇿🇲 زامبيا", callback_data=CB_ZAMBIA)],
        [InlineKeyboardButton("↩️ العودة الى القائمة الرئيسية", callback_data=CB_BACK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text="""
        💫 مرحبًا بك في قسم اشتراكات Starlink!

🌍 الرجاء اختيار الدولة التي تريد تفعيل أو تجديد الاشتراك فيها من القائمة أدناه:
        
        
        """,
        reply_markup=reply_markup
    )
    
    return STARLINK_MENU

async def usdt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("شراء دولار /USDT", callback_data=CB_BUY)],
        [InlineKeyboardButton("بيع دولار /USDT", callback_data=CB_SELL)],
        [InlineKeyboardButton("↩️ العودة الى القائمة الرئيسية", callback_data=CB_BACK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="""
        【★】AP Digital Store【★】

❖ بيع وشراء عملة USDT بثقة وسرعة ⚡
❖ نتعامل بـ الجنيه السوداني 🇸🇩 و الدرهم الإماراتي 🇦🇪 و الفرنك الرواندي 🇷🇼 
❖ أسعار مميزة وتحويلات فورية لأي محفظة
❖ دعم متواصل وخدمة عملاء على مدار الساعة
🚀 الوجهة الذكية لعالم العملات الرقمية
        """,
        reply_markup=reply_markup
    )
    return USDT_MENU

async def mbok_aed_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("أدفع درهم (AED) ⬅ أستلم جنيه (SDG)", callback_data=CB_MBOK_AED_SDG)],
        [InlineKeyboardButton("أدفع جنيه (SDG) ⬅ أستلم درهم (AED)", callback_data=CB_MBOK_SDG_AED)],
        [InlineKeyboardButton("↩️ العودة الى القائمة الرئيسية", callback_data=CB_BACK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="""
بنكك 💱 درهم إماراتي (AED)

الرجاء اختيار اتجاه التحويل الذي ترغب به:
""",
        reply_markup=reply_markup
    )
    return MBOKAED_MENU

async def ask_mbok_aed_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    flow_type = query.data # e.g., 'mbok_aed_sdg_flow'
    context.user_data['mbok_flow'] = flow_type
    
    if flow_type == CB_MBOK_AED_SDG:
        pay_currency = 'AED'
        receive_currency = 'SDG'
        rate = AED_TO_SDG_MORE # Using higher rate for calculation example
    else: # CB_MBOK_SDG_AED
        pay_currency = 'SDG'
        receive_currency = 'AED'
        rate = 1 / SDG_TO_AED
        
    context.user_data['pay_currency'] = pay_currency
    context.user_data['receive_currency'] = receive_currency
    context.user_data['rate'] = rate

    await query.edit_message_text(
        text=f"""
تحويل 
{receive_currency} ⬅ {pay_currency}

سعر الصرف:
1 {pay_currency} = {rate:.4f} {receive_currency}

الرجاء إدخال المبلغ الذي ترغب في دفعه بـ {pay_currency} للمتابعة:
(مثال: 500)
"""
    )
    return GET_AMOUNT_MBOK_AED # Move to the state that expects a text message

async def handle_mbok_aed_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int: 
    amount_str = update.message.text.strip()
    
    try:
        amount_to_pay = float(amount_str)
        if amount_to_pay <= 0:
            await update.message.reply_text("الرجاء إدخال مبلغ صحيح وموجب.")
            return GET_AMOUNT_MBOK_AED 

        pay_currency = context.user_data.get('pay_currency')
        receive_currency = context.user_data.get('receive_currency')
        rate = context.user_data.get('rate')
        link = USDT_AED_LINK # Use a relevant link for AED transactions
        
        amount_to_receive = amount_to_pay * rate
        
        response_text = f"""
✅تأكيد عملية التحويل

المبلغ الذي ستدفعه:
{amount_to_pay:,.2f} {pay_currency}

المبلغ الذي ستستلمه:
{amount_to_receive:,.2f} {receive_currency}

سعر الصرف:
{pay_currency} = {rate:,.4f} {receive_currency}

الخطوة التالية:
يرجى الضغط على الرابط أدناه للتواصل مع الإدارة وتأكيد عملية الدفع.
👇👇👇
{link}


أو يمكنك العودة إلى القائمة الرئيسية /start
"""
        await update.message.reply_text(response_text)
        
        
    except ValueError:
        await update.message.reply_text("خطأ! الرجاء إدخال رقم صحيح للمبلغ.")
        return GET_AMOUNT_MBOK_AED 

    context.user_data.clear() 
    return MAIN_MENU

async def mbok_rwf_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("أدفع فرنك (RWF) ⬅ أستلم جنيه (SDG)", callback_data=CB_MBOK_RWF_SDG)],
        [InlineKeyboardButton("أدفع جنيه (SDG) ⬅ أستلم فرنك (RWF)", callback_data=CB_MBOK_SDG_RWF)],
        [InlineKeyboardButton("↩️ العودة الى القائمة الرئيسية", callback_data=CB_BACK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="""
بنكك 💱 فرنك رواندي (RWF)

الرجاء اختيار اتجاه التحويل الذي ترغب به:
""",
        reply_markup=reply_markup
    )
    return MBOKRWF_MENU

async def ask_mbok_rwf_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    flow_type = query.data # e.g., 'mbok_rwf_sdg_flow'
    context.user_data['mbok_flow'] = flow_type
    
    if flow_type == CB_MBOK_RWF_SDG:
        pay_currency = 'RWF'
        receive_currency = 'SDG'
        rate = RWF_TO_SDG # Rate is 1 RWF to SDG
    else: # CB_MBOK_SDG_RWF
        pay_currency = 'SDG'
        receive_currency = 'RWF'
        rate = SDG_TO_RWF # Rate is 1 SDG to RWF
        
    context.user_data['pay_currency'] = pay_currency
    context.user_data['receive_currency'] = receive_currency
    context.user_data['rate'] = rate
    context.user_data['link'] = USDT_RWF_LINK # Use link for RWF transactions

    await query.edit_message_text(
        text=f"""
تحويل 
{receive_currency} ⬅ {pay_currency}

سعر الصرف  :
100,000 {pay_currency} = {100000*rate:,.2f} {receive_currency}

الرجاء إدخال المبلغ الذي ترغب في دفعه بـ {pay_currency} للمتابعة:
(مثال: 100000)
"""
    )
    return GET_AMOUNT_MBOK_RWF

async def handle_mbok_rwf_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    amount_str = update.message.text.strip()
    
    try:
        amount_to_pay = float(amount_str)
        if amount_to_pay <= 0:
            await update.message.reply_text("الرجاء إدخال مبلغ صحيح وموجب.")
            return GET_AMOUNT_MBOK_RWF

        pay_currency = context.user_data.get('pay_currency')
        receive_currency = context.user_data.get('receive_currency')
        rate = context.user_data.get('rate')
        link = context.user_data.get('link')
        
        amount_to_receive = amount_to_pay * rate
        
        response_text = f"""
✅ تأكيد عملية التحويل

المبلغ الذي ستدفعه :
{amount_to_pay:,.2f} {pay_currency}

المبلغ الذي ستستلمه:
{amount_to_receive:,.2f} {receive_currency}

سعر الصرف:
 {pay_currency} = {rate:,.3f} {receive_currency}

الخطوة التالية:
يرجى الضغط على الرابط أدناه للتواصل مع الإدارة وتأكيد عملية الدفع.
👇👇👇
{link}

أو يمكنك العودة إلى القائمة الرئيسية /start
"""
        await update.message.reply_text(response_text)
        
    except ValueError:
        await update.message.reply_text("خطأ! الرجاء إدخال رقم صحيح للمبلغ.")
        return GET_AMOUNT_MBOK_RWF

    context.user_data.clear() 
    return MAIN_MENU

async def show_usdt_buy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    buy_text = """
الرجاء اختيار العملة المحلية التي تود الشراء بها:
💰 خيارات التحويل المتوفرة :
 🇦🇪 الدرهم الإماراتي (AED)
 🇸🇩 الجنيه السوداني (SDG)
 🇷🇼 الفرنك الرواندي (RWF)
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
        [InlineKeyboardButton("🇦🇪 شراء بالدرهم الإماراتي", callback_data=f"{CB_AED}_BUY")],
        [InlineKeyboardButton("🇸🇩 شراء بالجنيه السوداني", callback_data=f"{CB_SDG}_BUY")],
        [InlineKeyboardButton("🇷🇼 شراء بالفرنك الرواندي", callback_data=f"{CB_RWF}_BUY")],
        [InlineKeyboardButton("↩️ العودة إلى القائمة", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=buy_text,
        reply_markup=reply_markup
    )
    
    return BUY_USDT_SUBMENU

async def ask_buy_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompts the user to enter the amount they want to pay."""
    query = update.callback_query
    await query.answer()
    currency_code = query.data.split('_')[0]
    context.user_data['currency_code'] = currency_code
    context.user_data['transaction_type'] = 'BUY'
    currency_map = {'AED': 'الدرهم الإماراتي', 'SDG': 'الجنيه السوداني', 'RWF': 'الفرنك الرواندي'}
    currency_name = currency_map.get(currency_code, 'العملة المحلية')
    rate = get_rate(currency_code, is_selling_usdt=False)
    await query.edit_message_text(
        text= f"""
📈 شراء USDT - الدفع بـ {currency_name} ({currency_code})

سعر الصرف الحالي:
1 USDT = {rate} {currency_code}

الرجاء إدخال المبلغ الذي ترغب في دفعه بـ {currency_code} لتحويله إلى USDT:
(مثال: 500)
"""
    )
    return GET_AMOUNT_BUY # Move to the state that expects a text message (the amount)

async def handle_buy_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Calculates the USDT amount and provides the link."""
    amount_str = update.message.text.strip()
    currency_code = context.user_data.get('currency_code')
    
    try:
        amount_to_pay = float(amount_str)
        if amount_to_pay <= 0:
            await update.message.reply_text("الرجاء إدخال مبلغ صحيح وموجب.")
            return GET_AMOUNT_BUY 
        rate = get_rate(currency_code, is_selling_usdt=False)
        usdt_amount = amount_to_pay / rate
        
        # 3. Get Link
        if currency_code == 'AED': link = USDT_AED_LINK
        elif currency_code == 'SDG': link = USDT_SDG_LINK
        elif currency_code == 'RWF': link = USDT_RWF_LINK
        else: link = tele_user
        
        # 4. Generate Final Message
        response_text = f"""
✅ تأكيد عملية الشراء

 المبلغ الذي ستدفعه: 
 {amount_to_pay:,.2f} {currency_code}
 
 المبلغ الذي ستحصل عليه :
 {usdt_amount:,.2f}  USDT
 
 سعر الصرف:  USDT = 
 {rate:,.2f} {currency_code}

الخطوة التالية:
يرجى الضغط على الرابط أدناه للتواصل مع الإدارة وتأكيد عملية الدفع والحصول على USDT.
👇👇👇
{link}

أو يمكنك العودة إلى القائمة الرئيسية /start
"""
        await update.message.reply_text(response_text)
    
    except ValueError:
        await update.message.reply_text("خطأ! الرجاء إدخال رقم صحيح للمبلغ.")
        return GET_AMOUNT_BUY
    
    # Clear user data and return to main menu state
    context.user_data.clear()
    return MAIN_MENU

def get_rate(currency_code, is_selling_usdt):
    """returns the correct rate based on the currency and transaction type"""
    if is_selling_usdt:
        if currency_code == CB_AED: return USDT_TO_AED
        if currency_code == CB_SDG: return USDT_TO_SDG
        if currency_code == CB_RWF: return USDT_TO_RWF
    else:
        if currency_code == CB_AED: return AED_TO_USDT
        if currency_code == CB_SDG: return SDG_TO_USDT
        if currency_code == CB_RWF: return RWF_TO_USDT
    return 1.0

async def show_usdt_sell(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    sell_text = """
الرجاء اختيار العملة المحلية التي تود التحويل إليها (استلام المبلغ بها):

💰 خيارات التحويل المتوفرة :
 🇦🇪 الدرهم الإماراتي (AED)
 🇸🇩 الجنيه السوداني (SDG)
 🇷🇼 الفرنك الرواندي (RWF)
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
        [InlineKeyboardButton("🇦🇪 بيع إلى الدرهم الإماراتي", callback_data=f"{CB_AED}_SELL")],
        [InlineKeyboardButton("🇸🇩 بيع إلى الجنيه السوداني", callback_data=f"{CB_SDG}_SELL")],
        [InlineKeyboardButton("🇷🇼 بيع إلى الفرنك الرواندي", callback_data=f"{CB_RWF}_SELL")],
        [InlineKeyboardButton("↩️ العودة إلى القائمة", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=sell_text,
        reply_markup=reply_markup
    )
    
    return SELL_USDT_SUBMENU

async def ask_sell_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompts the user to enter the USDT amount they want to sell."""
    query = update.callback_query
    await query.answer()
    
    # Extract the currency code from the callback data (e.g., 'AED_SELL')
    currency_code = query.data.split('_')[0]
    
    context.user_data['currency_code'] = currency_code
    context.user_data['transaction_type'] = 'SELL'
    
    currency_map = {'AED': 'الدرهم الإماراتي', 'SDG': 'الجنيه السوداني', 'RWF': 'الفرنك الرواندي'}
    currency_name = currency_map.get(currency_code, 'العملة المحلية')
    
    rate = get_rate(currency_code, is_selling_usdt=True)
    
    await query.edit_message_text(
        text= f"""
📉 بيع USDT - الاستلام بـ {currency_name} ({currency_code})

سعر الصرف الحالي:
1 USDT = {rate} {currency_code}

الرجاء إدخال المبلغ الذي ترغب في بيعه بـ USDT:
(مثال: 100)
"""
    )
    return GET_AMOUNT_SELL

async def handle_sell_amount(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    amount_str = update.message.text.strip()
    currency_code = context.user_data.get('currency_code')
    
    try:
        # 1. Validate Input
        usdt_amount = float(amount_str)
        if usdt_amount <= 0:
            await update.message.reply_text("الرجاء إدخال مبلغ صحيح وموجب.")
            return GET_AMOUNT_SELL # Stay in the same state
        
        # 2. Get Rate and Calculate
        rate = get_rate(currency_code, is_selling_usdt=True)
        amount_to_receive = usdt_amount * rate
        
        # 3. Get Link
        if currency_code == 'AED': link = USDT_AED_LINK
        elif currency_code == 'SDG': link = USDT_SDG_LINK
        elif currency_code == 'RWF': link = USDT_RWF_LINK
        else: link = tele_user
        
        # 4. Generate Final Message
        response_text = f"""
✅ تأكيد عملية البيع

المبلغ الذي ستبيعه :
{usdt_amount:,.2f} USDT
المبلغ الذي ستستلمه :
{amount_to_receive:,.2f} {currency_code}
سعر الصرف: 
1 USDT  = {rate:,.2f} {currency_code}

الخطوة التالية:
يرجى الضغط على الرابط أدناه للتواصل مع الإدارة وتأكيد عملية البيع واستلام المبلغ.
👇👇👇
{link}

أو يمكنك العودة إلى القائمة الرئيسية /start
"""
        await update.message.reply_text(response_text)
        
    except ValueError:
        await update.message.reply_text("خطأ! الرجاء إدخال رقم صحيح للمبلغ.")
        return GET_AMOUNT_SELL
    
    context.user_data.clear()
    return MAIN_MENU

async def show_buy_aed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
        ✨    AP Digital Store™    ✨
             ===========================
        💵  الدولار مقابل ⬅ الدرهم الإماراتي 🇦🇪
             ===========================
                1 USDT = {AED_TO_USDT} AED
             ===========================   
                             ⬇ اطلب الأن  
              {USDT_AED_LINK} 
            """
    keyboard = [
        
        [InlineKeyboardButton("↩️ Back to USDT Menu", callback_data=CB_BACK_USDT)]
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await  query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return BUY_USDT_SUBMENU

async def show_buy_sdg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text =  f"""
    ✨  AP Digital Store™  ✨
          ===========================
      💵  الدولار مقابل ⬅الجنيه السوداني 
          ===========================
                1 USDT = {SDG_TO_USDT} SDG
          ===========================
                        ⬇ اطلب الأن  
              {USDT_SDG_LINK} 
           """
    keyboard = [
        
        [InlineKeyboardButton("↩️ Back to USDT Menu", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return BUY_USDT_SUBMENU

async def show_buy_rwf(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
     ✨  AP Digital Store™  ✨
            ===========================
      الفرنك الرواندي 🇷🇼 مقابل ⬅ الدولار 💵 
            ===========================
                1 USDT = {RWF_TO_USDT} RWF
            ===========================
                           ⬇ اطلب الأن  
              {USDT_RWF_LINK}
           """
    keyboard = [
        [InlineKeyboardButton("↩️ Back to USDT Menu", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return BUY_USDT_SUBMENU

async def show_sell_aed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
       ✨  AP Digital Store™  ✨
            ===========================
      الدرهم الإماراتي 🇦🇪 مقابل⬅ 💵  الدولار   
             ===========================
                 1 USDT = {USDT_TO_AED} AED
             ===========================   
                             ⬇ اطلب الأن  
              {USDT_AED_LINK}
           """
    keyboard = [
    
        [InlineKeyboardButton("↩️ Back to USDT Menu", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return SELL_USDT_SUBMENU

async def show_sell_sdg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
     ✨   AP Digital Store™   ✨
           ===========================
      💵  الدولار مقابل ⬅الجنيه السوداني 
           ===========================
             1 USDT = {USDT_TO_SDG} SDG
           ===========================
                         ⬇ اطلب الأن  
              {USDT_SDG_LINK}
    
           """
    keyboard = [
        
        [InlineKeyboardButton("↩️ Back to USDT Menu", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return SELL_USDT_SUBMENU

async def show_sell_rwf(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
    ✨ AP Digital Store™  ✨
             ===========================
      💵  الدولار مقابل ⬅ الفرنك الرواندي 🇷🇼 
             ===========================
                1 USDT = {USDT_TO_RWF} RWF
             ===========================
                             ⬇ اطلب الأن  
              {USDT_RWF_LINK}
           """
    keyboard = [
        [InlineKeyboardButton("↩️ Back to USDT Menu", callback_data=CB_BACK_USDT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return SELL_USDT_SUBMENU

async def show_argentina_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
    🌍 Roam Unlimited
🇦🇷 87,500 ARS
━━━━━━━━━━━━━━
💵 Roam Unlimited
76 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*76} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━

💬 الأسعار تشمل العمولة

تجديد الاشتراك : ⬇
{ARGENTINA_LINK}
    
    
    """
                 
    # Recreate the Starlink menu keyboard to keep the Back button visible
    keyboard = [
        
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return STARLINK_SUBMENU

async def show_rwanda_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
    🌍 Roam Unlimited
🇷🇼 128,000 RWF
━━━━━━━━━━━━━━
💵 Roam Unlimited
100 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*100} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة

تجديد الاشتراك : ⬇
{RWANDA_LINK}
    
    
    """
                 
    # Recreate the Starlink menu keyboard to keep the Back button visible
    keyboard = [
        
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return STARLINK_SUBMENU # Stay in the Starlink menu state

async def show_kenya_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text = f"""
    🌍 Roam Unlimited
🇰🇪 14,000 KES
━━━━━━━━━━━━━━
💵 Roam Unlimited
122 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*122} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{KENYA_LINK}
    
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def show_hatiti_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Shows the tanzania price details."""
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
    🌍 Roam Unlimited
💵 85 USD
━━━━━━━━━━━━━━
💵 Roam Unlimited
95 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*95} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{HAITI_LINK}
    
    """
                
    
    # Recreate the Starlink menu keyboard
    keyboard = [

        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def show_malawi_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
    🌍 Roam Unlimited
🇲🇼 170,000 MWK
━━━━━━━━━━━━━━
💵 Roam Unlimited
111 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*111} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{MALAWI_LINK}
    
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
    
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def show_philippines_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
    🌍 Roam Unlimited
🇵🇭 ₱5,700
━━━━━━━━━━━━━━
💵 Roam Unlimited
109 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*109} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{PHILIPPINES_LINK}
    
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
    
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def shwo_mozambique(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    price_text =  f"""
    🌍 Roam Unlimited
🇲🇿 6,000 MZN
━━━━━━━━━━━━━━
💵 Roam Unlimited
107 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*107} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{MOZAMBIQUE_LINK}
    
    """
    keyboard = [
    
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    return STARLINK_SUBMENU

async def show_peru_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
     🌍 Roam Unlimited
🇵🇪 335 PEN
━━━━━━━━━━━━━━
💵 Roam Unlimited
107 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*107} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{PERU_LINK}
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
    
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def show_zambia_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
    🌍 Roam Unlimited
🇿🇲 2,500 ZMW
━━━━━━━━━━━━━━
💵 Roam Unlimited
123 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*123} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{ZAMBIA_LINK}
  
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [

        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def show_yemen_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
    🌍 Roam Unlimited
🇾🇪 100 USD
━━━━━━━━━━━━━━
💵 Roam Unlimited
110 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*110} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{YEMEN_LINK}
    
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [

        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

async def show_europe_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    query = update.callback_query
    await query.answer()
    
    price_text = f"""
    🌍 Roam Unlimited
💶 89 EUR
━━━━━━━━━━━━━━
💵 Roam Unlimited
116 USDT (بالدولار الرقمي)
━━━━━━━━━━━━━━
🇸🇩 Roam Unlimited
{SDG_TO_USDT*116} SDG (بالجنيه السوداني)
━━━━━━━━━━━━━━
💬 الأسعار تشمل العمولة
تجديد الاشتراك : ⬇
{EUROPE_LINK}
    
    
    """
    
    # Recreate the Starlink menu keyboard
    keyboard = [
    
        [InlineKeyboardButton("العودة الى قائمة الدول ↩️", callback_data=CB_BACK_STARLINK_COUNTRIES)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=price_text,
        reply_markup=reply_markup
    )
    
    return STARLINK_SUBMENU

# --- Fallback/Exit Function (e.g., for /cancel) ---
async def end_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ends the conversation by sending a simple farewell message."""
    await update.message.reply_text("Goodbye! Feel free to type /start again.")
    return ConversationHandler.END

# --- Unhandled Text Message (Generic fallback) ---
async def handle_unhandled_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responds to text that is not a command or callback."""
    await update.message.reply_text("عذراً...الرجاء إختيار احد الأوامر أو الضغط على /start للبدء من جديد")
   
def main() -> None:
    app = Application.builder().token(TOKEN).build()
    
    # Define the ConversationHandler
    conv_handler = ConversationHandler (
        
        # 1. Entry Point: Starts the conversation with /start
        entry_points=[CommandHandler('start', start_command)],

        # 2. States: Define what handlers are active in each menu state
        states={
            MAIN_MENU: [
                # Handler for Starlink button: moves to the STARLINK_MENU state
                CallbackQueryHandler(starlink_command, pattern='^' + CB_STARLINK + '$'),
                CallbackQueryHandler(usdt_command, pattern='^' + CB_USDT + '$'),
                CallbackQueryHandler(mbok_aed_command, pattern='^' + CB_MBOK_AED + '$'),
                CallbackQueryHandler(mbok_rwf_command, pattern='^' + CB_MBOK_RWF + '$'),
                CommandHandler('start', start_command),
            ],
            
            STARLINK_MENU: [
                # Handlers for country price details
                CallbackQueryHandler(show_argentina_price, pattern='^' + CB_ARGENTINA + '$'),
                CallbackQueryHandler(show_europe_price, pattern='^' + CB_EUROPE + '$'),
                CallbackQueryHandler(show_hatiti_price, pattern='^' + CB_HAITI + '$'),
                CallbackQueryHandler(show_kenya_price, pattern='^' + CB_KENYA + '$'),
                CallbackQueryHandler(show_malawi_price, pattern='^' + CB_MALAWI + '$'),
                CallbackQueryHandler(shwo_mozambique, pattern='^' + CB_MOZAMBIQUE + '$'),
                CallbackQueryHandler(show_peru_price, pattern='^' + CB_PERU + '$'),
                CallbackQueryHandler(show_rwanda_price, pattern='^' + CB_RWANDA + '$'),
                CallbackQueryHandler(show_philippines_price, pattern='^' + CB_THE_PHILIPPINES + '$'),
                CallbackQueryHandler(show_yemen_price, pattern='^' + CB_YEMEN + '$'),
                CallbackQueryHandler(show_zambia_price, pattern='^' + CB_ZAMBIA + '$'),
                # Handler for the 'Back' button: returns to the MAIN_MENU state
                CallbackQueryHandler(start_command, pattern='^' + CB_BACK + '$'),
                CommandHandler('start', start_command),
            ],
            
            STARLINK_SUBMENU:[
                CallbackQueryHandler(show_argentina_price, pattern='^' + CB_ARGENTINA),
                CallbackQueryHandler(show_europe_price, pattern='^' + CB_EUROPE),
                CallbackQueryHandler(show_hatiti_price, pattern='^' + CB_HAITI),
                CallbackQueryHandler(show_kenya_price, pattern='^' + CB_KENYA),
                CallbackQueryHandler(show_malawi_price, pattern='^' + CB_MALAWI),
                CallbackQueryHandler(shwo_mozambique, pattern='^' + CB_MOZAMBIQUE),
                CallbackQueryHandler(show_peru_price, pattern='^' + CB_PERU),
                CallbackQueryHandler(show_rwanda_price, pattern='^' + CB_RWANDA),
                CallbackQueryHandler(show_philippines_price, pattern='^' + CB_THE_PHILIPPINES),
                CallbackQueryHandler(show_yemen_price, pattern='^' + CB_YEMEN),
                CallbackQueryHandler(show_zambia_price, pattern='^' + CB_ZAMBIA),
                CallbackQueryHandler(starlink_command, pattern='^' + CB_BACK_STARLINK_COUNTRIES),
                CommandHandler('start', start_command),
                
            ],
            
            USDT_MENU: [
                CallbackQueryHandler(show_usdt_sell, pattern='^' + CB_SELL + '$'),
                CallbackQueryHandler(show_usdt_buy, pattern= '^' + CB_BUY + '$'),
                CallbackQueryHandler(start_command, pattern='^' + CB_BACK + '$'),
                CommandHandler('start', start_command),
            ],
            
            BUY_USDT_SUBMENU: [
                CallbackQueryHandler(ask_buy_amount, pattern= f'^{CB_AED}_BUY$'),
                CallbackQueryHandler(ask_buy_amount, pattern=f'^{CB_SDG}_BUY$'),
                CallbackQueryHandler(ask_buy_amount, pattern=f'^{CB_RWF}_BUY$'),
                CallbackQueryHandler(usdt_command, pattern='^' + CB_BACK_USDT + '$'),
                CommandHandler('start', start_command),
                
                
            ],
            
            SELL_USDT_SUBMENU: [
                CallbackQueryHandler(ask_sell_amount, pattern=f'^{CB_AED}_SELL$'),
                CallbackQueryHandler(ask_sell_amount, pattern=f'^{CB_SDG}_SELL$'),
                CallbackQueryHandler(ask_sell_amount, pattern=f'^{CB_RWF}_SELL$'),
                CallbackQueryHandler(usdt_command, pattern='^' + CB_BACK_USDT + '$'),
                CommandHandler('start', start_command),
                
            ],
            
            GET_AMOUNT_BUY: [
              MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buy_amount),
              CallbackQueryHandler(usdt_command, pattern='^' + CB_BACK_USDT + '$'),
              CommandHandler('start', start_command),  
            ],
            
            GET_AMOUNT_SELL: [
              MessageHandler(filters.TEXT & ~filters.COMMAND, handle_sell_amount),
              CallbackQueryHandler (usdt_command, pattern='^' + CB_BACK_USDT + '$'),
              CommandHandler('start', start_command), 
            ],
            
            MBOKAED_MENU:[

                CallbackQueryHandler(ask_mbok_aed_amount, pattern='^' + CB_MBOK_AED_SDG + '$'),
                CallbackQueryHandler(ask_mbok_aed_amount, pattern='^' + CB_MBOK_SDG_AED + '$'),
                CallbackQueryHandler(start_command, pattern='^' + CB_BACK + '$'),
                CommandHandler('start', start_command),
            ],
            
            MBOKRWF_MENU: [
                CallbackQueryHandler(ask_mbok_rwf_amount, pattern='^' + CB_MBOK_RWF_SDG + '$'),
                CallbackQueryHandler(ask_mbok_rwf_amount, pattern='^' + CB_MBOK_SDG_RWF + '$'),
                CallbackQueryHandler(start_command, pattern='^' + CB_BACK + '$'),
                CommandHandler('start', start_command),
            
            ],
            
            GET_AMOUNT_MBOK_AED: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_mbok_aed_amount),
                CommandHandler('start', start_command),
            ],
            
            GET_AMOUNT_MBOK_RWF: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_mbok_rwf_amount),
                CommandHandler('start', start_command),
            ],
        
        },
        
        # 3. Fallbacks: Define commands that can end the conversation (e.g., /cancel)
        fallbacks=[CommandHandler('cancel', end_conversation)],
    )

    # Add the main Conversation Handler
    app.add_handler(conv_handler)
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_unhandled_text))
    
    # Add a final generic message handler for unhandled text, placed AFTER the ConversationHandler
    print('starting bot...')
    print('Polling...')
    app.run_polling(poll_interval=2)
       
if __name__== '__main__':
    main()

