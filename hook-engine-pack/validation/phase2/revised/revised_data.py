# v1.1.0 outputs for B01-B13, produced by following the REVISED Hook Engine instructions. B11-B13 are the held-out briefs (their v1.0 baselines were frozen before any change).
# Author-generated (language model); Iraqi Arabic is a draft needing native review. Same-model generation + review = bias risk (see report).
def F(id, hook, gloss, mech, key, pkey, gap, carrier, frame, cont, payoff, beats, claims, risk, conf, aih=False, b2=""):
    return dict(id=id, hook=hook, gloss=gloss, mech=mech, key=key, pkey=pkey, gap=gap, carrier=carrier, frame=frame, cont=cont, payoff=payoff,
                beats=beats, claims=claims, risk=risk, conf=conf, aih=aih, b2=b2)
def C(text, src, quote, scope, st="verified", form="assertion", in_hook=True):
    return (text, src, st, form, in_hook, quote, scope)

BRIEFS = [
 dict(id="B01", title="Pinhole demo", audience="Iraqi adults 18-40, many wear glasses", platform="YouTube Short", dur=30, held_out=False,
  brief="Show that a small hole in a card makes blurred text readable. Phone, printed line, card.",
  verdict="PROCEED. Angle a standard explainer lacks: the size trade-off (why ~1.2 mm, not smaller) and where the clue fails. Confidence: مرجح.",
  terms=["ثقب","السطر","الثقب"], rec="A", why="clearest visual with an honest control; later finalists carry the size and limits stories",
  fin=[
   F("A","نفس السطر. نفس الكاميرا. شنو تغيّر؟","Same line, same camera. What changed?","M11","pinhole-aperture","aperture-shrinks-blur",
     "What did the card with a hole change?","frame","Defocused printed line; black card with a ~1 mm hole enters from the right; the line becomes readable (optics demo, labelled)",
     "Control: the same card without a hole changes nothing","Mechanism: smaller aperture, smaller blur spots; costs light",
     [("0-3","hook + reveal","line sharpens when the holed card enters","نفس السطر. نفس الكاميرا. شنو تغيّر؟"),
      ("3-8","control","the same card without a hole changes nothing; the hole is the variable","الورقة بدون ثقب ما تسوي شي. الثقب هو الفرق."),
      ("8-17","mechanism","each object point becomes a blur spot; a narrow aperture makes the spot smaller","كل نقطة تصير بقعة مشوشة، والثقب يضيّق الشعاع فتصغر البقعة."),
      ("17-24","cost","less light reaches the sensor/eye, so the image is dimmer","وتدفع ثمنها: ضوء أقل، فالصورة تصير أغمق."),
      ("24-30","limit + re-hook","this is an optics demo not an eye test; clinics use a specific size","هذا شرح بصريات مو فحص نظر. وبالعيادة يستعملون حجم معيّن — ليش؟")],
     [C("A small aperture can make blur from a focusing error look sharper","S45","people with a refractive error, such as myopia, can usually see better with the pinhole","clinical pinhole test; refractive error; shown here with a defocused camera as an optics analogy"),
      C("Decreasing pupil size increases depth of focus","S46","Decreasing pupil size increases the depth of focus","StatPearls pupil-size chapter; optics principle")],
     "A camera's defocus is an analogy, not the viewer's eye","مرجح"),
   F("B","ليش ثقب العيادة ١.٢ ملم؟ لو أصغر… يصير أسوأ.","Why is the clinic hole 1.2 mm? Smaller makes it worse.","M04","pinhole-size-tradeoff","why-not-smaller",
     "Why would a smaller hole be worse?","voice","Three cards with holes of decreasing size photographed through the same defocused lens; the smallest is dark and soft",
     "Diffraction and brightness","Why ~1.2 mm is the working size",
     [("0-4","hook + contrast","a middle hole is sharp; a tiny hole is darker and softer","ليش ثقب العيادة ١.٢ ملم؟ لو أصغر… يصير أسوأ."),
      ("4-12","evidence of the effect","the smallest hole looks worse than the middle one on camera","شوف: الثقب الأصغر أغمق وأنعم من الوسط."),
      ("12-21","reason","below about 0.75 mm diffraction blurs the image again and the view darkens","تحت حدود ٠.٧٥ ملم، الضوء ينثني على الحافة فالصورة تتشوّش مرة ثانية."),
      ("21-27","working size","clinical occluders use about 1.2 mm","عيادات النظر تستقر على حوالي ١.٢ ملم."),
      ("27-30","close","optics is a trade-off","بالبصريات دايماً اكو ثمن لكل تحسين.")],
     [C("Clinical pinhole is about 1.2 mm; smaller apertures add diffraction blur","S65","if the pinhole aperture is smaller than 1.2 millimeters, the blurring effects of diffraction","clinical pinhole for refractive-error assessment; Whitney 2009 tested 0.5-1.5 mm; Kim 2014 reports blur below ~0.75 mm"),
      C("Apertures below ~0.75 mm cause considerable diffraction blurring","S66","aperture size smaller than 0.75 mm causes considerable diffraction blurring","IOVS 2014 pinhole-glasses study discussion",in_hook=False)],
     "Hard to film the three sizes legibly (marked UNFILMABLE if the smallest hole is not visible on camera)","مرجح"),
   F("C","ثقب يحسّن النظر عند ناس… ويخرّبه عند ناس. ليش؟","A pinhole improves sight for some people and worsens it for others. Why?","M04","pinhole-clue-limits","clinical-clue-and-its-limits",
     "Why does the same hole help some people and not others?","voice","Clinician-style hand holding a pinhole occluder in front of an eye-chart line, then a second line that does not improve",
     "If blur is from focusing error it improves; some eye conditions do not","Clue vs diagnosis",
     [("0-4","hook","the same device gives opposite results","ثقب يحسّن النظر عند ناس… ويخرّبه عند ناس. ليش؟"),
      ("4-12","case 1","with a focusing error, acuity usually improves through the hole","إذا التشويش من التركيز، الثقب يساعد."),
      ("12-20","case 2","with macular disease or lens opacities the pinhole may not help or may worsen","وإذا اكو مشكلة بالشبكية أو العدسة، ممكن ما يساعد أو يخرّب."),
      ("20-27","why clinicians use it","the result is a clue under controlled conditions that guides the next test","الدكتور يستعمله كمؤشر، وبعدها يكمّل الفحص."),
      ("27-30","close (not a self-test)","a home attempt cannot tell you which case you are","وبالبيت ما تگدر تعرف أنت أي حالة. الفحص هو الجواب.")],
     [C("Through a pinhole, vision improves with refractive error and may be unchanged or worse with macular disease","S68","Worse vision might indicate macular diseases or lens opacities","pinhole test discussion in a keratoconus paper; WHO uses it in rapid surveys; not accurate for estimating post-refraction acuity"),
      C("Individuals with macular disease may have similar or even reduced acuity through a pinhole","S65","may have similar or even reduced acuity through a pinhole","clinical teaching document; macular and other central-vision disease")],
     "Could be misread as a self-test; closing beat must hold","مرجح")]),
 dict(id="B02", title="Why eyes burn after reels", audience="Iraqi 18-35 heavy phone users", platform="Instagram Reel", dur=25, held_out=False,
  brief="Explain why eyes feel tired or burning after long scrolling without scaring people or pushing glasses.",
  verdict="PROCEED. Angle: let the viewer observe their own blinking (participatory) and keep the blue-light myth as a separate hook. Confidence: مرجح.",
  terms=["عيون","ريلز","رمش","ترمش","20"], rec="B", why="participatory and self-evidencing; A and C carry different takeaways",
  fin=[
   F("A","ليش عيونك تحرگ بعد ريلز… ومو بسبب الضوء الأزرق؟","Why do your eyes burn after reels - and it is not the blue light?","M02","blue-light-not-cause","cause-is-use-not-light",
     "If not blue light, then what?","voice","Phone in dark room with blue-light filter toggled; on-screen `ضوء أزرق؟`","AAO attribution on screen","Cause is how we use screens (blinking), not blue light",
     [("0-3","hook","negates the popular cause","ليش عيونك تحرگ بعد ريلز… ومو بسبب الضوء الأزرق؟"),
      ("3-9","authority","AAO: digital eye discomfort is not caused by blue light","الأكاديمية الأمريكية لطب العيون تگول: التعب مو من الضوء الأزرق."),
      ("9-17","real driver","we blink less when staring at screens, so the surface dries","السبب انك ترمش أقل لما تطالع الشاشة، فالسطح يناشف."),
      ("17-22","what helps","breaks and looking away; artificial tears per AAO","استراحات، وطالع بعيد، ودموع اصطناعية إذا ناشفة."),
      ("22-25","close","discomfort is temporary but persistent symptoms deserve an exam","وإذا استمر التعب، راجع مختص نظر.")],
     [C("AAO: digital eye discomfort is not caused by blue light","S32","Digital eye discomfort is not caused by blue light","AAO digital devices page, Dec 2025; screen use in adults"),
      C("We blink less when staring at screens","S32","blink rate can be cut in half when staring at screens","AAO page; population-level statement",in_hook=False)],
     "Same domain as B; payoffs differ (cause vs self-observation)","مرجح"),
   F("B","عدّ كم مرة ترمش بدقيقة ريلز.","Count how many times you blink in a minute of reels.","M10","blink-self-count","your-own-count-vs-normal",
     "Is my number low?","frame","Reel playing; blink counter overlay starting at 0; the narrator counts silently","Compare your count with the usual rate","What a 'low' count means and does not mean",
     [("0-3","hook + task","viewer is asked to count","عدّ كم مرة ترمش بدقيقة ريلز."),
      ("3-14","observe","a minute of scrolling with the counter visible","(ريلز بدقيقة — العدّاد يشتغل)"),
      ("14-19","benchmark","normal blink rate is around 15 per minute and can be cut in half at screens","الطبيعي حوالي ١٥ بالدقيقة، وبالشاشة ينزل للنص تقريباً."),
      ("19-23","meaning","fewer blinks dry the surface; this is not a diagnosis","هذا مو تشخيص، بس يفسّر ليش تحرگ."),
      ("23-25","close","one habit to try","جرّب ترمش عمداً بعد كل شاشة، وشوف الفرق.")],
     [C("Normal blink rate is around 15 per minute and can be cut in half at screens","S32","Normally, we blink around 15 times per minute","AAO digital devices page; adults; 15 blinks per minute normal")],
     "A self-count is imprecise; must not be framed as a test","مرجح"),
   F("C","قاعدة ٢٠-٢٠-٢٠: تنفع لو بس نصيحة؟","The 20-20-20 rule: does it work or is it just advice?","M08","twenty-twenty-twenty-evidence","what-is-recommended-vs-proven",
     "Is there evidence behind the rule?","voice","Timer overlay while someone looks out of a window","AAO recommends it; efficacy evidence needs retrieval","What the rule is, who recommends it, what is not shown",
     [("0-4","hook","asks about evidence","قاعدة ٢٠-٢٠-٢٠: تنفع لو بس نصيحة؟"),
      ("4-11","rule","every 20 minutes look at something 20 feet away for 20 seconds","كل ٢٠ دقيقة، طالع شي بعيد ٢٠ قدم لمدة ٢٠ ثانية."),
      ("11-18","status","AAO recommends it; efficacy trials must be sourced before publishing (RESEARCH)","الأكاديمية توصي بيها، وأنا راح أجيب الدراسات قبل لا أگول إنها مثبتة."),
      ("18-23","fallback","other AAO tips that do not depend on the rule: blink, distance, lighting","وتوصيات ثانية: رمش، مسافة ٢٥ إنج، وإضاءة مناسبة."),
      ("23-25","close","tell the viewer what is proven and what is advice","النصيحة موجودة، والإثبات نشوفه بالمصدر.")],
     [C("AAO recommends the 20-20-20 rule","S33","Take regular breaks using the “20-20-20” rule","AAO 2021; screen users; recommendation, efficacy not reviewed")],
     "Payoff incomplete until the efficacy evidence is retrieved (marked RESEARCH)","تخمين")]),
 dict(id="B03", title="Blue-light glasses", audience="Iraqi 20-40 considering glasses", platform="TikTok", dur=30, held_out=False,
  brief="Evidence-based take on blue-light glasses; no brands.",
  verdict="PROCEED. Angle: why the evidence is hard to trust (masking problem), not just 'AAO says no'. Confidence: مرجح.",
  terms=["نظارة","الضوء الأزرق","شبكية","نظارات"], rec="A", why="original angle with a visual (clear vs yellow lens) and an accurate, hedged payoff",
  fin=[
   F("A","كيف تسوي تجربة على نظارة الضوء الأزرق… واللابس يعرف إنها الحقيقية؟","How do you run a trial of blue-light glasses when the wearer knows they are the real ones?","M20","blinding-problem","why-trials-are-weak",
     "Why is it hard to test them fairly?","voice","A clear lens beside a yellow-tinted lens held to the camera","Yellow tint prevents masking","Why the evidence is weak without saying they are useless",
     [("0-5","hook + visual","clear vs yellow lens","كيف تسوي تجربة على نظارة الضوء الأزرق… واللابس يعرف إنها الحقيقية؟"),
      ("5-12","the problem","these lenses are yellow, so participants can tell which pair they got","لأنها صفرة، المشارك يعرف أي نظارة لبس."),
      ("12-19","what else limits studies","studies are small and short","والدراسات صغيرة وقصيرة."),
      ("19-26","what is concluded","a 2023 review found no consistent evidence of benefit for eye strain; AAO does not recommend special eyewear for screens","مراجعة ٢٠٢٣ ما لقت دليل ثابت، والأكاديمية ما توصي بيها."),
      ("26-30","close","absence of strong evidence is not proof of harm; habits help","مو معناها مضرّة، معناها الدليل ضعيف. والعادات أوضح فايدة.")],
     [C("Blue-blocking lens studies used yellow-tinted lenses, limiting masking","S34","all of these studies have used yellow-tinted blue-blocking lenses, limiting the adequate masking","2023 narrative review citing Lawrenson et al.; small (<50) short studies"),
      C("No consistent evidence supports blue-blocking spectacle lenses for eye strain","S34","there is no consistent evidence to support the use of blue-blocking filters in spectacle lenses","2023 narrative review (not systematic)",in_hook=False)],
     "Long hook (13 content words); needs a read-aloud trim","مرجح"),
   F("B","قبل النوم، المشكلة مو نظارتك. هي ساعات الشاشة.","Before bed the issue isn't your glasses - it's screen hours.","M16","sleep-timing-not-glasses","screen-timing-for-sleep",
     "What should I do for sleep then?","text","On-screen text: `نظارة ← نوم؟` crossed out, then a clock","AAO advice on timing","Practical sleep advice with attribution",
     [("0-4","hook","reframes the cause","قبل النوم، المشكلة مو نظارتك. هي ساعات الشاشة."),
      ("4-12","evidence","some evidence that blue light affects the sleep-wake cycle (AAO)","الأكاديمية تگول اكو دليل إن الضوء يأثر على دورة النوم."),
      ("12-20","advice","avoid screens two to three hours before bed; use night mode","ابتعد عن الشاشة ٢-٣ ساعات گبل النوم، وفعّل الوضع الليلي."),
      ("20-26","why not glasses","AAO says sleep can be improved without special glasses","ما تحتاج نظارة خاصة حسب الأكاديمية."),
      ("26-30","close","a realistic nightly plan","جرّب اليوم، وشوف.")],
     [C("AAO advises avoiding screens two to three hours before bed","S33","avoid using screens two to three hours before bed","AAO 2021; adults; 2-3 hours")],
     "Sleep is adjacent to the brief; kept because glasses are marketed for sleep","مرجح"),
   F("C","الضوء الأزرق من شاشتك يضر شبكيتك؟ الدليل لحد الآن ما يقول هيچ.","Does your screen's blue light harm your retina? The evidence so far doesn't say so.","M08","no-retinal-link","no-meaningful-link-to-retina",
     "What does the evidence say about retinal damage?","voice","Phone beside a retina diagram with a question mark","Lab studies did not mimic screens","What is and isn't known",
     [("0-4","hook","asks and answers carefully","الضوء الأزرق من شاشتك يضر شبكيتك؟ الدليل لحد الآن ما يقول هيچ."),
      ("4-12","why people worry","lab and animal studies showed cell damage in dishes","التجارب بالأطباق والحيوانات شافت ضرر."),
      ("12-19","why it doesn't transfer","those studies did not mimic screen exposure","بس ما قلّدت ضوء الشاشات الحقيقي."),
      ("19-26","unknowns","long-term cumulative effects are unknown","والأثر الطويل المدى لسه مجهول."),
      ("26-30","close","sun overexposure is the proven risk","الشمس بدون حماية أخطر من الشاشة.")],
     [C("So far the evidence shows no meaningful link between blue light and damage to human retinas","S32","the evidence shows no meaningful link between blue light and: damage to human retinas","AAO Dec 2025; screens; lab/animal studies did not mimic screens"),
      C("Overexposure to sun blue/UV can raise eye-disease risk","S32","overexposure to blue light and UV light rays from the sun can raise the risk of eye disease","AAO",in_hook=False)],
     "Last line 'الشمس أخطر' compares two exposures not directly measured in the source; soften or source before publishing","مرجح")]),
 dict(id="B04", title="Myopia-control lenses for parents", audience="Iraqi parents of children 6-12", platform="YouTube Short", dur=40, held_out=False,
  brief="Educate parents about myopia progression options. No brands or clinics.",
  verdict="PROCEED with MANDATORY professional review (paediatric treatment). Confidence: مرجح.",
  terms=["قصر النظر","طفل","نظارة","برا"], rec="B", why="corrects a harmful habit with sourced evidence and a clear action",
  fin=[
   F("A","٢٣ دراسة على ١٣ ألف طفل… شنو يعني \"تبطّئ\" قصر النظر؟","23 trials on 13k children... what does 'slows' myopia mean?","M18","lenses-average-effect","what-slowing-means",
     "What does 'slow' mean for my child?","voice","Number counter, then an animated eye growing slightly longer with and without special lenses","Average effect is modest and design-dependent","Quantified meaning of 'slow' and what it is not",
     [("0-6","hook","numbers raise a question","٢٣ دراسة على ١٣ ألف طفل… شنو يعني \"تبطّئ\" قصر النظر؟"),
      ("6-14","what myopia progression is","the eye grows longer, power increases","قصر النظر يتقدم لما العين تطول."),
      ("14-24","quantified","on average axial length growth is ~0.15 mm less and refraction ~0.31 D less than with single-vision lenses","بالمتوسط العين تطول أقل بحوالي ٠.١٥ ملم، وتقدّم القوة أقل بحوالي ٠.٣ دايوبتر."),
      ("24-33","limits","slowing, not stopping; designs differ; individual response varies","هذا تبطئة مو إيقاف، وتختلف حسب التصميم والطفل."),
      ("33-40","close","decision belongs to the child's eye professional","القرار مع مختص يفحص طفلك.")],
     [C("Specialty lenses slowed progression on average in 23 RCTs","S39","23 RCTs with a total of 13.315 subjects","children and adolescents; pooled vs single-vision lenses; AL -0.15 mm, SER -0.31 D; design-specific")],
     "Paediatric advice; review required","مرجح"),
   F("B","تقليل قوة نظارة الطفل ما يبطّئ قصر النظر… وممكن يسرّعه.","Under-correcting a child's glasses doesn't slow myopia and may speed it.","M02","undercorrection-myth","use-the-full-prescription",
     "Is that really true?","text","Parent adjusting child's glasses (staged) with `أقل قوة = أبطأ؟` on screen","RCT evidence","Why full correction is advised",
     [("0-4","hook","","تقليل قوة نظارة الطفل ما يبطّئ قصر النظر… وممكن يسرّعه."),
      ("4-12","why parents try it","belief that weaker lenses 'rest' the eye","كثير أهل يفكرون إن النظارة الأضعف ترتاح بيها العين."),
      ("12-24","what trials found","binocular undercorrection did not slow progression and may accelerate it","التجارب لقت إنها ما تبطّئ، وبعضها لقى تسارع."),
      ("24-33","what is different","specialty lenses are designed differently; they are not 'weaker glasses'","عدسات التحكم بقصر النظر مصممة بشكل ثاني، مو نظارة أضعف."),
      ("33-40","close","use the prescribed power and ask about options","استعمل القوة المكتوبة، واسأل المختص عن الخيارات.")],
     [C("Binocular undercorrection does not slow myopia progression and may accelerate it","S41","undercorrection does not slow myopia progression; instead, it may even accelerate the progression","review of RCTs; children; one paired-eye monovision study showed the opposite for the undercorrected eye")],
     "Review excerpt only (primary RCTs not opened)","مرجح"),
   F("C","وقت العطلة برا البيت… هل يغيّر قصر النظر عند الطفل؟","Holiday time outdoors... does it change a child's myopia?","M08","outdoor-time","outdoor-time-evidence",
     "Does outdoor time really matter?","voice","Children on a school playground in bright light","Seven RCTs in China","Evidence and its limits",
     [("0-4","hook","","وقت العطلة برا البيت… هل يغيّر قصر النظر عند الطفل؟"),
      ("4-14","evidence","7 randomized trials, 9,437 children: lower incidence of myopia","٧ تجارب عشوائية على أكثر من ٩٠٠٠ طفل: اقل ظهور لقصر النظر."),
      ("14-26","limits","all trials in China; dose unclear; mixed evidence once a child is already myopic","كلها بالصين، وما نعرف الجرعة، والأثر على اللي عنده قصر نظر أضعف."),
      ("26-34","safety","sun protection matters","وانتبه للشمس: قبعة ونظارة بحماية UV."),
      ("34-40","close","one realistic target","جرّب تزيد وقت اللعب برا بشكل منتظم.")],
     [C("More outdoor time lowered myopia incidence in children in 7 RCTs","S40","seven randomized controlled trials involving a total of 9,437 subjects","children; all trials conducted in China; RR 0.84 for incidence"),
      C("Outdoor-time effect on children who are already myopic is mixed","S41","Whether the protective effect ... extends to those who are already myopic is equivocal","review")],
     "Iraqi heat/UV context not covered by the trials","مرجح")]),
 dict(id="B05", title="Eye chart letters", audience="Iraqi 18-40", platform="Instagram Reel", dur=25, held_out=False,
  brief="Make the eye chart interesting; visual explainer with a printed chart.",
  verdict="RE-ANGLE (chart explainers saturated) -> two non-obvious facts: the 1/5 geometry and why 6 m; PROCEED. Confidence: مرجح.",
  terms=["لوحة","حروف","السطر","متر"], rec="C", why="a question most explainers do not answer, with a source and a physical reason",
  fin=[
   F("A","ليش سماكة خط الحرف بلوحة الفحص بالضبط خُمس ارتفاعه؟","Why is the stroke of a chart letter exactly one fifth of its height?","M05","letter-geometry","detail-equals-one-arcminute",
     "Why that ratio?","voice","Chart letter with a grid overlay highlighting stroke and gap widths","Critical detail = 1/5 height","Geometry ties to one arcminute",
     [("0-3","hook","","ليش سماكة خط الحرف بلوحة الفحص بالضبط خُمس ارتفاعه؟"),
      ("3-10","show","stroke and gap are each one fifth of the height","السماكة والفتحة، كل وحدة خُمس الارتفاع."),
      ("10-18","reason","at 6/6 each stroke subtends one arcminute","عند ٦/٦ كل خط يشغل دقيقة قوسية واحدة."),
      ("18-22","consequence","the test asks if you can resolve that detail","الفحص يسأل: تگدر تفرّق هذي التفاصيل؟"),
      ("22-25","close","a tidy design behind a simple chart","وراء اللوحة هندسة مدروسة.")],
     [C("Snellen letters have critical detail equal to one fifth of letter height","S47","subtends 1/5th of the overall height","Snellen design; at 6/6 stroke subtends one arcminute")],
     "'خُمس' may be unfamiliar; test spoken phrasing","مرجح"),
   F("B","السطر يُحسب مقروء إذا قريت أكثر من نصف حروفه — حسب معيار ١٩٨٤.","A line counts as read if you read more than half its letters, per a 1984 standard.","M01","line-scoring-rule","how-scoring-works",
     "So how exact is 20/20?","frame","Chart line with some letters struck out and a `؟` on screen","Standard rule vs modern practice","The scoring convention and its date",
     [("0-4","hook","","السطر يُحسب مقروء إذا قريت أكثر من نصف حروفه — حسب معيار ١٩٨٤."),
      ("4-12","example","read 3 of 5 and the line counts","قريت ٣ من ٥؟ السطر يُحسب."),
      ("12-19","date and scope","this is the 1984 ICO standard; practice varies today","هذا معيار ١٩٨٤، والممارسة اليوم تختلف."),
      ("19-23","meaning","20/20 is a convention, not a razor-sharp threshold","فـ٢٠/٢٠ اتفاق عملي، مو خط حاد."),
      ("23-25","close","exams add other tests","وبالفحص الكامل اكو اختبارات ثانية.")],
     [C("A line counts as read when more than 50% of its optotypes are read (1984 ICO standard)","S43","considered to have been read correctly when more than 50%","1984 International Council of Ophthalmology standard text; clinical practice varies")],
     "Source copy hosted on an unusual domain","مرجح"),
   F("C","ليش فحص النظر يصير على ٦ أمتار؟","Why is the eye test done at 6 metres?","M05","why-six-metres","relaxed-focus-at-distance",
     "Why 6 m and not 3?","voice","Tape measure from chart to chair labelled 6 m","Accommodation relaxed","The physical reason for the distance",
     [("0-3","hook","","ليش فحص النظر يصير على ٦ أمتار؟"),
      ("3-10","tape measure","the chair is 6 m from the chart","الكرسي على ٦ أمتار بالضبط."),
      ("10-18","reason","looking far relaxes the focusing muscle so the eye is tested without extra focusing","لأن النظر البعيد يريّح عضلة التركيز، فنفحص العين من غير تركيز زايد."),
      ("18-23","same in feet","20 feet is the same distance","وبالقدم هي ٢٠ قدم — ولهذا ٢٠/٢٠."),
      ("23-25","close","clinics without space use mirrors","والعيادات الصغيرة تستعمل مراية.")],
     [C("The eye is tested looking at distance (usually 6 metres) so the focusing muscle is relaxed","S94","measured looking in the distance (usually 6 metres) so that the ciliary muscle is relaxed","teaching article; far-point testing"),
      C("20 feet equals 6 metres (20/20 = 6/6)","S47","6/6 (20/20)","Snellen notation in metres and feet",in_hook=False),
      C("Clinics with limited space use mirrors","S94","(no source retrieved)","script-only claim, unverified",st="unverified",in_hook=False)],
     "Mirror line unsourced (script-only, marked)","مرجح")]),
 dict(id="B06", title="Blind spot", audience="Iraqi 16-45, curious", platform="TikTok", dur=30, held_out=False,
  brief="Interactive demo: viewer finds their own blind spot. Include why we do not notice it.",
  verdict="PROCEED (S69-S71); mechanism hedged because filling-in is debated. Confidence: مرجح.",
  terms=["غمّض","عين","خنصر","القمر","ثقب","نظرك"], rec="A", why="no screen geometry needed; sourced finger demo",
  fin=[
   F("A","غمّض عينك اليسار، مدّ إيدك اليمين، وطالع بظفر إبهامك… خنصرك راح يختفي.","Close your left eye, extend your right arm, look at your thumbnail... your little finger will vanish.","M10","blind-spot-finger-demo","where-the-blind-spot-is",
     "Why does it vanish?","voice","Close-up of a hand with spread fingers; the pinky wiggles and fades out of focus (illustrative)","Optic nerve head has no photoreceptors","Where it is and why it is there",
     [("0-5","hook + instruction","viewer does the steps","غمّض عينك اليسار، مدّ إيدك اليمين، وطالع بظفر إبهامك… خنصرك راح يختفي."),
      ("5-12","do it","spread fingers, wiggle the little finger","فرّد أصابعك وحرّك الخنصر… شفته يختفي؟"),
      ("12-20","why","the optic nerve leaves the retina there; no photoreceptors","هناك العصب البصري يطلع من الشبكية، وماكو خلايا تشوف."),
      ("20-26","size","about 6 degrees across - room for a dozen moons side by side","حجمه حوالي ٦ درجات — يكفي لـ١٢ قمر بجنب بعض."),
      ("26-30","close","this is normal anatomy; it differs from a disease finding","هذا تشريح طبيعي موجود عند الكل.")],
     [C("Little finger vanishes at the blind spot when the other eye is closed","S69","Now wiggle your little finger. It will fall on your blind spot","left eye closed, right arm extended, gaze on thumbnail; Anstis 2010 primer")],
     "Geometry works for the right eye with left closed; reverse for left","مرجح"),
   F("B","ليش ما تشوف ثقب بنص نظرك؟","Why don't you see a hole in your vision?","M04","brain-fills-in","brain-fills-in-the-gap",
     "Why is there no visible hole?","voice","A striped pattern with a gap that visually closes (illustration)","Perceptual filling-in; debated mechanism","What filling-in is and is not known",
     [("0-3","hook","","ليش ما تشوف ثقب بنص نظرك؟"),
      ("3-11","fact","each eye has a spot without photoreceptors","بكل عين اكو بقعة بدون خلايا مستقبلة."),
      ("11-19","filling-in","the area looks filled with the surrounding colour or texture","الدماغ يعبّيها بلون وملمس اللي حواليها."),
      ("19-25","debate","how exactly is debated","وكيف يسويها بالضبط لسه نقاش علمي."),
      ("25-30","close with action","gaps from retinal problems can also be filled in, so routine eye exams matter","وحتى فجوات المرض ممكن تنملأ، لهذا الفحص الدوري مهم.")],
     [C("The blind spot appears filled in with the colour or texture of the surround","S69","looks ‘filled-in’ with the color or texture of the surround","Anstis 2010; mechanism debated (Durgin 1995)"),
      C("Scotomas from retinal damage or glaucoma are also filled in, so patients may not notice","S69","a scotoma is also perceptually filled-in, so effectively that the patient is often not aware","primer statement; closing beat only, attributed",in_hook=False)],
     "The closing health line must stay attributed and action-oriented","مرجح"),
   F("C","البقعة العمياء بعرض ٦ درجات… تخبّي ١٢ قمر!","The blind spot is 6 degrees wide - enough to hide 12 moons!","M01","blind-spot-size","size-comparison",
     "How can something that big go unnoticed?","frame","12 moons lined up across a circle on a night-sky photograph (illustration)","Size comparison","Scale of the blind spot",
     [("0-4","hook","","البقعة العمياء بعرض ٦ درجات… تخبّي ١٢ قمر!"),
      ("4-12","proof by comparison","each moon is ~0.5 degree, so a dozen fit","القمر نص درجة تقريباً، فـ١٢ يكفون."),
      ("12-20","why unnoticed","the other eye covers the area and the brain fills it in","العين الثانية تغطيها، والدماغ يعبّيها."),
      ("20-27","check it","try the finger demo from the previous video","جرّب تجربة الخنصر اللي بالفيديو السابق."),
      ("27-30","close","size is normal","وهذا طبيعي عند كل الناس.")],
     [C("The blind spot is about 6 degrees in diameter, large enough to hold a dozen moons","S69","about 6° in diameter — large enough to hold a dozen moons side by side","Anstis 2010 primer; a dozen = 12 moons")],
     "Moon size (~0.5 degree) is general knowledge not in the source; script-only","مرجح")]),
 dict(id="B07", title="Colour-vision plate tests", audience="Iraqi adults and parents", platform="YouTube Short", dur=35, held_out=False,
  brief="Explain what Ishihara-type plates do and do not tell you, including online versions.",
  verdict="PROCEED, professional review flag (diagnostic language). Angle: plates miss some cases; online can't diagnose. Confidence: مرجح.",
  terms=["لوحات","الألوان","اختبار","أحمر"], rec="A", why="a precise, surprising limit with a sourced number",
  fin=[
   F("A","لوحات الألوان تكشف ٩٦٪ بس من الحالات… ليش مو ١٠٠؟","Colour plates detect only about 96% of cases... why not 100%?","M08","plates-miss-some","why-screening-is-not-diagnosis",
     "Why do plates miss some people?","voice","Ishihara-style plate (own artwork) with `96%` counter","Screening vs diagnosis","What screening can and cannot tell",
     [("0-4","hook","","لوحات الألوان تكشف ٩٦٪ بس من الحالات… ليش مو ١٠٠؟"),
      ("4-12","what plates are","dots hide a number; red-green screening","نقاط ملونة تخفي رقم، وتفحص الأحمر والأخضر."),
      ("12-21","why some are missed","some mild cases read the hidden digits; some normal people misread a plate","بعض الحالات الخفيفة تقرأ الرقم، وبعض الناس الطبيعيين يغلطون."),
      ("21-28","what diagnoses","an anomaloscope is the clinical instrument","التشخيص النهائي بجهاز اسمه anomaloscope."),
      ("28-35","close","a plate result is a prompt to get examined, not a verdict","نتيجة اللوحة تنبيه، مو حكم.")],
     [C("Plate tests detect about 96% of cases confirmed by anomaloscope","S74","detect about 96 percent of the cases confirmed by anomaloscope","validated plate series (Ishihara, Dvorine, AO H-R-R); red-green congenital defects")],
     "Source is an older report; confirm against a recent source before publishing","مرجح"),
   F("B","أغلب عمى الألوان يشوف ألوان — بس بشكل مختلف.","Most colour blindness still sees colour - just differently.","M02","partial-colour","most-see-colour",
     "What do they actually see?","frame","Split image: normal vs a simulated deficiency (clearly labelled `محاكاة`)","Simulation caveat","Corrects the black-and-white myth",
     [("0-4","hook","","أغلب عمى الألوان يشوف ألوان — بس بشكل مختلف."),
      ("4-13","myth","most colour-blind people see partial colour","الأغلبية تشوف ألوان جزئية."),
      ("13-22","typical confusion","reds and greens can look similar","الأحمر والأخضر يتشابهون."),
      ("22-29","caveat","a simulation is an approximation, not what a person sees","هذي محاكاة تقريبية، مو بالضبط اللي يشوفه الشخص."),
      ("29-35","close","rare complete forms exist","والنوع الكامل نادر.")],
     [C("Most people who are colour blind see partial colour","S35","Most people who are color blind see partial color","AAO myths page 2022; myth 9")],
     "Simulations can mislead; label them","مرجح"),
   F("C","اختبار ألوان على موبايلك… شنو ما يگدر يگوله لك؟","A colour test on your phone... what can't it tell you?","M08","online-test-limits","online-tests-cannot-diagnose",
     "What can't a phone test tell me?","voice","Phone showing a plate, `تشخيص؟` crossed out","Cleveland Clinic: online tests cannot diagnose","Limits and the next step",
     [("0-4","hook","","اختبار ألوان على موبايلك… شنو ما يگدر يگوله لك؟"),
      ("4-12","what they are","examples of what real tests look like","هي أمثلة تشبه الفحص الحقيقي."),
      ("12-21","limit","online tests can't diagnose","بس ما تشخّص."),
      ("21-28","why","screen colours and conditions vary; diagnosis needs a trained examiner","ألوان الشاشة تختلف، والتشخيص يحتاج مختص."),
      ("28-35","close","if you suspect a problem, book an exam","إذا شاكك، احجز فحص.")],
     [C("Online colour tests can't diagnose","S73","But they can’t diagnose anything.","Cleveland Clinic patient page 2023; online tests"),
      C("Ishihara identifies red-green deficiency only","S73","Ishihara tests only diagnose red-green color deficiency.","Cleveland Clinic",in_hook=False)],
     "Secondary (health-system) source; the 'screen colours vary' reason is script-only reasoning","مرجح")]),
 dict(id="B08", title="Sleeping in contact lenses", audience="Iraqi 18-35 lens wearers", platform="Instagram Reel", dur=35, held_out=False,
  brief="Public-health style education, no fear-mongering, no brands.",
  verdict="PROCEED, MANDATORY professional review (infection risk). US data labelled. Confidence: مرجح.",
  terms=["العدسة","العدسات","النوم","تنام","نمت"], rec="A", why="surprising, sourced, and action-oriented",
  fin=[
   F("A","حتى العدسة المخصصة للنوم… خطرها أعلى؟ CDC تگول نعم.","Even lenses made for sleeping carry higher risk? CDC says yes.","M20","overnight-lens-risk","overnight-approved-lenses-still-riskier",
     "Is an 'approved for sleep' lens safe to sleep in?","voice","Lens case labelled `extended wear` on a bedside table","Class 3 device","Why approval does not erase the risk",
     [("0-4","hook","","حتى العدسة المخصصة للنوم… خطرها أعلى؟ CDC تگول نعم."),
      ("4-12","what 'approved' means","some lenses are FDA-approved for overnight wear","بعض العدسات مصرّح بيها للنوم."),
      ("12-22","the catch","risk is higher regardless of lens material; classed among the highest-risk device group","بس الخطر أعلى مهما كان نوع العدسة."),
      ("22-30","what to do","sleep in lenses only if your provider directs you","لا تنام بالعدسة إلا إذا الطبيب يوصي."),
      ("30-35","close","red or painful eye: remove lenses and see a provider","عين حمرا أو ألم؟ شيل العدسة وراجع مختص.")],
     [C("Sleeping in lenses is a risk factor regardless of lens material","S76","Sleeping in lenses has been shown to be a risk factor regardless of lens material","CDC MMWR 2018; US; observational; overnight-approved lenses are Class 3 devices"),
      C("Avoid sleeping in lenses unless directed by your eye care provider","S75","Avoid sleeping in lenses unless directed by your eye care provider.","CDC guidance 2025",in_hook=False)],
     "US data; Iraq regulation of overnight lenses unverified","مرجح"),
   F("B","نمت ساعة بالعدسة؟ حتى النوم النادر يرفع الخطر.","Napped an hour in your lenses? Even occasional sleep raises the risk.","M09","occasional-sleep-risk","even-naps-count",
     "Does a nap really matter?","frame","Person dozing on a sofa; lens case on the table; text `قيلولة؟`","Risk with even occasional overnight use","Naps count; what to do",
     [("0-4","hook","","نمت ساعة بالعدسة؟ حتى النوم النادر يرفع الخطر."),
      ("4-13","evidence","risk increases even with occasional overnight use","حتى مرة ومرة تزيد الخطر."),
      ("13-21","size","about six- to eightfold higher infection risk (US observational estimate)","حوالي ٦ لـ٨ أضعاف بالبيانات الأمريكية."),
      ("21-29","practical","set a reminder; carry glasses and a case","حط تذكير، وخلّي النظارة وياك."),
      ("29-35","close","symptoms mean remove and call","إذا احمرار أو ألم، شيل العدسة وراجع.")],
     [C("Even occasional overnight use confers risk","S76","even occasional overnight use conferring risk","CDC MMWR 2018 citing prior studies; US")],
     "'Napping an hour' is the creator's framing; CDC speaks of sleeping or napping","مرجح"),
   F("C","نص لابسي العدسات بأمريكا نام بيها مرة. وانت؟","Half of US lens wearers have slept in them. And you?","M09","how-common","you-are-not-alone-but-it-matters",
     "Am I the only one?","voice","Survey-style counter filling to 50%","Prevalence","Prevalence is not safety",
     [("0-4","hook","","نص لابسي العدسات بأمريكا نام بيها مرة. وانت؟"),
      ("4-12","data","a 2014 US survey: 50% ever slept in lenses","استبيان أمريكي ٢٠١٤: ٥٠٪ نامو بيها."),
      ("12-21","not safe because common","common behaviour with a high relative risk","شائعة، بس خطرها عالي."),
      ("21-29","habits","remove lenses nightly; replace case regularly","شيل العدسة كل ليلة، وبدّل العلبة."),
      ("29-35","close","talk to your provider about your own schedule","احچي مع مختصك عن جدولك.")],
     [C("In a 2014 US survey 50% of wearers reported ever sleeping in lenses","S77","In 2014, 50% of contact lens wearers reported ever sleeping in contact lenses","CDC MMWR 2019 citing a 2014 US survey; not Iraq")],
     "US number for an Iraqi audience: scope must be stated on screen","مرجح")]),
 dict(id="B09", title="Presbyopia", audience="Iraqi 38-55", platform="TikTok", dur=30, held_out=False,
  brief="Why people past 40 hold phones farther away. Reassuring, not scary.",
  verdict="PROCEED (S78-S80). Angle: timeline (when it stops worsening) + caveat. Confidence: مرجح.",
  terms=["الموبايل","القراية","عدسة","تبعّد"], rec="A", why="relatable, reassuring, with its caveat in the same beat",
  fin=[
   F("A","تبعّد الموبايل حتى تقرأ؟ هذا غالباً عمر… والحل بسيط.","Holding your phone away to read? Probably age - and the fix is simple.","M09","presbyopia-normal-fixable","normal-and-fixable-with-caveat",
     "What changed?","voice","Arm extended, phone far, text slightly blurred then clear with reading glasses","Age-related loss of near focus","Name, cause, fix, caveat",
     [("0-4","hook","","تبعّد الموبايل حتى تقرأ؟ هذا غالباً عمر… والحل بسيط."),
      ("4-11","name","presbyopia is a normal part of aging","اسمها presbyopia، وهي جزء طبيعي من العمر."),
      ("11-19","cause","after 40 the lens becomes more rigid","بعد الأربعين العدسة تصير أقسى."),
      ("19-26","fix","glasses, contacts, medication or surgery","نظارة قراءة أو عدسات، وفي خيارات ثانية."),
      ("26-30","caveat (same beat)","blurred near vision still deserves an exam; earlier onset can go with farsightedness or diabetes","بس التشويش دايماً يستاهل فحص، وإذا قبل الأربعين لازم تراجع.")],
     [C("Presbyopia is a normal part of aging","S79","It is a normal part of aging.","AAO 2026; onset shortly after 40; earlier onset possible (Mayo S80)")],
     "Reassurance requires the caveat beat to survive editing","مرجح"),
   F("B","بعد الأربعين عدسة عيونك تصير أقسى… شلون يأثر هذا على القراءة؟","After 40 your lens gets stiffer... how does that affect reading?","M05","lens-stiffness-mechanism","how-focusing-works",
     "How does a stiffer lens blur near text?","voice","Animated lens: round when young, flatter and stiff after 40","Accommodation mechanism","How focusing at near works and fails",
     [("0-4","hook","","بعد الأربعين عدسة عيونك تصير أقسى… شلون يأثر هذا على القراءة؟"),
      ("4-12","how it works","a muscle reshapes the lens to focus near","عضلة تلف العدسة حتى تركز على القريب."),
      ("12-20","what changes","a stiffer lens cannot reshape enough","العدسة الأقسى ما تتغير بما يكفي."),
      ("20-26","result","light focuses behind the retina; text blurs","الضوء يتركز ورا الشبكية، فيتشوش الحرف."),
      ("26-30","close","distance helps temporarily; glasses fix it","التبعيد يساعد مؤقتاً، والنظارة تحلها.")],
     [C("After age 40 the lens becomes more rigid","S79","After age 40, the lens becomes more rigid.","AAO 2026"),
      C("Muscle contraction makes the lens rounder for near focus","S80","making the lens more rounded","Mayo; accommodation",in_hook=False)],
     "Beat 2 re-asks via the mechanism","مرجح",aih=True,b2="How does the focusing muscle reshape the lens in the first place?"),
   F("C","القراية القريبة تصعب وتصعب… ومتى تتوقف؟","Near reading keeps getting harder... when does it stop?","M08","presbyopia-timeline","progression-stops-around-65",
     "When does it stop worsening?","voice","Timeline from 40 to 65+ with a reading chart","NEI timeline","Progression timeline and onset variability",
     [("0-4","hook","","القراية القريبة تصعب وتصعب… ومتى تتوقف؟"),
      ("4-12","onset","usually after about 40-45","تبدي غالباً بعد الأربعين-الخمسة وأربعين."),
      ("12-20","progression","gets worse over time","وتسوء مع الوقت."),
      ("20-27","stop","usually stops getting worse after age 65","وغالباً تتوقف بعد عمر ٦٥."),
      ("27-30","close","update glasses as it changes","غيّر النظارة حسب التغيير.")],
     [C("Presbyopia usually stops getting worse after age 65","S78","usually stops getting worse after age 65","NEI; general; agencies differ on onset (40 vs 45)")],
     "Onset differs between NEI (after 45) and AAO (after 40): state both","مرجح")]),
 dict(id="B10", title="Phoropter: one or two?", audience="Iraqi adults anxious about eye tests", platform="YouTube Short", dur=30, held_out=False,
  brief="Explain why the test asks 'which is better, one or two?' and reassure viewers who are unsure.",
  verdict="PROCEED (practitioner sources S81-S83, labelled). Confidence: تخمين/مرجح.",
  terms=["واحد","اثنين","الجهاز","فحص"], rec="A", why="reassurance with an honest allowed answer ('about the same')",
  fin=[
   F("A","\"واحد لو اثنين؟\" وانت مو متأكد؟ هذا متوقع.","\"One or two?\" and you're not sure? That's expected.","M13","unsure-is-expected","neither-is-crystal-clear",
     "Is it okay to be unsure?","voice","Phoropter close-up, lenses flipping; viewer POV","Examiner script","Why unsure happens and what to answer",
     [("0-4","hook","","\"واحد لو اثنين؟\" وانت مو متأكد؟ هذا متوقع."),
      ("4-12","clinician reports","patients often can't decide which is better","كثير مرضى ما يگدرون يقررون."),
      ("12-20","what examiners say","neither choice will be crystal clear","الفاحص يگولك: ولا وحدة راح تكون صافية تماماً."),
      ("20-27","allowed answer","'about the same' is acceptable","وإذا نفسهم، گول: نفس الشي."),
      ("27-30","close","answer honestly","جاوب بصدق، والباقي على الفاحص.")],
     [C("Patients often cannot decide 'one or two'","S81","they can’t decide “which is better, one or two”","trade-journal clinician report; practitioner evidence, not a trial")],
     "Practitioner evidence only","تخمين"),
   F("B","بفحص الاستجماتزم، الفرق بين \"واحد\" و\"اثنين\" أكبر مما تحس — ليش؟","In astigmatism testing the difference between 'one' and 'two' is bigger than you feel - why?","M05","jcc-step","why-the-choices-are-exaggerated",
     "If it feels small, why is it large?","voice","Handheld Jackson cross-cylinder flipping in front of a lens","JCC mechanism","A mechanism that explains the odd question",
     [("0-5","hook","","بفحص الاستجماتزم، الفرق بين \"واحد\" و\"اثنين\" أكبر مما تحس — ليش؟"),
      ("5-13","tool","a Jackson cross-cylinder flips two lens versions","أداة اسمها Jackson cross-cylinder تقلب بين خيارين."),
      ("13-22","numbers","a +0.25 D cross-cylinder gives a whole-diopter difference between the choices","فرق ٠.٢٥ بالأداة يعطي فرق دايوبتر كامل بين الخيارين."),
      ("22-27","why","a big enough difference lets you compare without moving focus off the retina","حتى تگدر تقارن بدون ما يطلع التركيز عن الشبكية."),
      ("27-30","close","this is one step among several","وهذي خطوة وحدة من خطوات.")],
     [C("A traditional +0.25 D JCC gives a whole-diopter difference between the two choices","S82","A traditional +0.25 D JCC actually gives a whole diopter difference","trade article 2008; Jackson cross-cylinder step; astigmatism refinement")],
     "Technical for laypeople","تخمين"),
   F("C","شوف الصورتين… أي أوضح؟ (مو فحص — بس تحس الإحساس).","Look at the two images - which is clearer? (not a test - just the feeling).","M23","small-differences","just-noticeable-difference",
     "Can I tell them apart?","frame","Two slightly different blurred lines labelled 1 and 2","JND","Why small differences are hard",
     [("0-4","hook + disclaimer","","شوف الصورتين… أي أوضح؟ (مو فحص — بس تحس الإحساس)."),
      ("4-12","viewer tries","the images differ by a small step","الفرق صغير جداً."),
      ("12-21","concept","just-noticeable difference: the smallest change that produces an effect","اسمه JND — أقل فرق ينحس."),
      ("21-27","relevance","why examiners use clear steps","لهذا الفاحص يخلي الفرق واضح."),
      ("27-30","close","the real exam is done with calibrated lenses","الفحص الحقيقي بعدسات مضبوطة.")],
     [C("Just-noticeable difference is the minimal amount of change needed to produce an effect","S81","just-noticeable differences” (JND), or the minimal amount of change needed to produce an effect","trade article; refraction context")],
     "Screen A/B rendering is a simulation; disclaimer must stay","تخمين")]),
 dict(id="B11", title="Astigmatism", audience="Iraqi adults 18-40", platform="Instagram Reel", dur=30, held_out=True,
  brief="Explain what astigmatism is in a visual way; no diagnosis from symptoms.",
  verdict="PROCEED (S84-S86). Confidence: مرجح.", terms=["قرنية","استجماتزم","الاستجماتزم","الأطفال","رگبي"], rec="A", why="visual and sourced",
  fin=[
   F("A","ليش قرنية بشكل كرة الرگبي تخلي النظر مشوّش قريب وبعيد؟","Why does a rugby-ball-shaped cornea blur both near and far?","M05","two-curvatures","blur-at-all-distances",
     "Why both near and far?","voice","A basketball and a rugby ball rotating with light rays overlaid","Mismatched curvature","Mechanism of blur at all distances",
     [("0-4","hook","","ليش قرنية بشكل كرة الرگبي تخلي النظر مشوّش قريب وبعيد؟"),
      ("4-12","normal eye","round surfaces bend light equally to one focus","السطح المدور يجمع الضوء بنقطة وحدة."),
      ("12-21","astigmatism","two curves bend light differently; two focus points","منحنيين مختلفين يعطون نقطتين تركيز."),
      ("21-27","correction","glasses with a cylindrical lens compensate","عدسة اسطوانية تعوّض."),
      ("27-30","close","symptoms need an exam to confirm","والأعراض لحالها ما تأكّد، الفحص يأكّد.")],
     [C("Astigmatism is an imperfection in the curvature of the cornea or lens; near and far vision are blurry","S84","With either type of astigmatism, near and far vision is blurry","AAO 2025; analogy: football vs basketball")],
     "Analogy invites self-diagnosis if not framed; closing beat holds","مرجح"),
   F("B","القراية بضوء خافت أو الجلوس گريب من التلفزيون… ما يسبب الاستجماتزم.","Reading in dim light or sitting close to the TV doesn't cause astigmatism.","M02","astigmatism-myths","what-doesnt-cause-it",
     "So what does?","frame","Child close to a TV with `شنو يسببه؟` on screen","AAO myth","What doesn't and what might",
     [("0-4","hook","","القراية بضوء خافت أو الجلوس گريب من التلفزيون… ما يسبب الاستجماتزم."),
      ("4-12","AAO","it's a myth","الأكاديمية الأمريكية تسميها خرافة."),
      ("12-21","what is known","risk is inherited; disease, injury or surgery can also cause it","الخطر يتوارث، ويمكن من مرض أو إصابة أو عملية."),
      ("21-27","child sitting close","may signal a vision problem worth checking","الطفل اللي يگعد گريب يستاهل فحص."),
      ("27-30","close","","الفحص يطمّنك.")],
     [C("Reading in low light or sitting close to the TV does not cause astigmatism","S84","It is a myth that reading in low light or sitting very close","AAO 2025")],
     "Last beat spoken line is short (3 words)","مرجح"),
   F("C","ليش الأطفال بالاستجماتزم ما يشتكون من التشويش؟","Why don't children with astigmatism complain about blur?","M20","kids-dont-complain","why-child-exams-matter",
     "Why are they silent?","voice","Child squinting at a whiteboard (staged)","Children don't know normal","Why exams, not symptoms, find it",
     [("0-4","hook","","ليش الأطفال بالاستجماتزم ما يشتكون من التشويش؟"),
      ("4-12","reason","they may not realize they see blurry","لأن الطفل ما يعرف إن اللي يشوفه مو طبيعي."),
      ("12-21","consequence","untreated astigmatism can affect school or sports and lead to amblyopia","ممكن يأثر بالدراسة أو الرياضة وحتى الكسل البصري."),
      ("21-28","action","a comprehensive eye exam finds it","فحص النظر الشامل يلقاه."),
      ("28-30","close","","فحص طفلك يوفر عليه سنين.")],
     [C("Children may not realize they have blurry vision and are unlikely to complain","S84","Children may not realize they have blurry vision","AAO 2025; children"),],
     "Paediatric; review; wording 'يوفر عليه سنين' is rhetorical","مرجح")]),
 dict(id="B12", title="Sunglasses", audience="Iraqi adults, hot sunny climate", platform="YouTube Short", dur=30, held_out=True,
  brief="What matters when choosing sunglasses; no brands.",
  verdict="PROCEED (S87-S90). Confidence: مرجح.", terms=["نظارة","UV","الشمس","ملصق","عدسة"], rec="A", why="counterintuitive, sourced, with an explicit comparator",
  fin=[
   F("A","نظارة شمس غامقة بدون فلتر UV… ممكن تدخّل أشعة أكثر لعينك؟","Dark sunglasses without a UV filter - could they let more rays into your eye?","M01","dark-without-uv","tint-is-not-protection",
     "More than what?","voice","Dark lens next to a clear lens, both held to the sun (illustrative)","Pupil dilates","Label vs tint",
     [("0-4","hook","","نظارة شمس غامقة بدون فلتر UV… ممكن تدخّل أشعة أكثر لعينك؟"),
      ("4-12","logic","darker view -> pupil stays larger","النظر الغامق يخلي البؤبؤ أكبر."),
      ("12-21","consequence","if UV is not filtered, more unfiltered UV can enter","وإذا ماكو فلتر، يدخل UV أكثر."),
      ("21-27","what to check","the label says 100% UV or UV400","دوّر على 'UV400' أو '100% UV'."),
      ("27-30","close","tint is not protection","اللون الغامق مو حماية.")],
     [C("Dark glasses without UV filtering may put eyes at greater risk because pupils stay larger","S87","Dark glasses that do not filter UV light may actually put your eyes at greater risk","AAO Q&A 2021; single ophthalmologist answer; comparator = wearing nothing/clear lenses is implied not stated"),],
     "Comparator not stated in the source; hook is a question and the video says 'may'","مرجح"),
   F("B","شنو الملصق الي يخلي نظارتك تحمي فعلاً؟","Which label makes your sunglasses actually protect?","M08","uv-label","read-the-label",
     "Which label?","frame","Close-up of a lens sticker with the code blurred, then revealed","Standards","How to read the protection claim",
     [("0-3","hook","","شنو الملصق الي يخلي نظارتك تحمي فعلاً؟"),
      ("3-10","reveal","UV400 or 100% UV protection","UV400 أو 100% UV."),
      ("10-19","what it means","100% UV: transmittance below 0.05% up to 380 nm","يعني السماحية أقل من ٠.٠٥٪ لحد ٣٨٠ نانومتر."),
      ("19-26","not tint, not price","protection depends on material and coating, not darkness or price","الحماية من المادة، مو من الغمق ولا السعر."),
      ("26-30","close","check wear: protection fades and scratches reduce it","والخدوش والزمن يقللون الحماية.")],
     [C("Sunglasses labelled UV400 or 100% UV protect regardless of fanciness or darkness","S88","As long as they are labeled with “UV400” or “100% UV protection”","AAO 2022; no brands used"),
      C("100% UV = transmittance below 0.05% up to 380 nm","S90","transmittance at wavelengths up to 380 nm is less than 0.05%","ISO 12312-1:2022 as summarised by Swiss BAG",in_hook=False)],
     "None major","مرجح"),
   F("C","عدسة UV لاصقة لحالها ما تكفي. عيونك وجلدك حواليها مكشوفين.","A UV contact lens alone isn't enough: your eye surface and the skin around it stay exposed.","M02","uv-contacts-not-enough","need-sunglasses-too",
     "What stays unprotected?","text","Eye close-up with the covered cornea highlighted and the rest shaded; text `الباقي؟`","Coverage","What contacts don't cover",
     [("0-4","hook","","عدسة UV لاصقة لحالها ما تكفي. عيونك وجلدك حواليها مكشوفين."),
      ("4-12","what they cover","only the cornea area","تغطي القرنية بس."),
      ("12-21","what remains","eyelid, conjunctiva and surrounding skin","الجفن والملتحمة والجلد حواليها."),
      ("21-27","best practice","sunglasses labelled UV400 plus a hat","نظارة UV400 وقبعة."),
      ("27-30","close","","احمي عيونك وجلدك سوا.")],
     [C("UV-blocking contacts leave the eyelid, conjunctiva and surrounding skin exposed","S88","leave the outside of the eye — including the eyelid, conjunctiva and surrounding skin — exposed","AAO 2022 quote of an ophthalmologist")],
     "Last spoken line short (4 words)","مرجح")]),
 dict(id="B13", title="Watery eyes and dryness", audience="Iraqi adults", platform="TikTok", dur=25, held_out=True,
  brief="Explain why dry eyes can feel watery; no diagnosis.",
  verdict="PROCEED (S91-S93), professional-review flag for persistent tearing. Confidence: مرجح.", terms=["دموع","تدمّع","دمعة","الدمعة","عيون"], rec="A", why="paradox, sourced, with scope 'one common cause'",
  fin=[
   F("A","ممكن عيونك تدمّع لأنها ناشفة. شلون؟","Your eyes may water because they are dry. How?","M04","dry-eye-paradox","reflex-tearing",
     "How can dry eyes water?","voice","Eye in wind with tear running, then a dry-surface close-up","Reflex tearing","Mechanism, with scope",
     [("0-3","hook","","ممكن عيونك تدمّع لأنها ناشفة. شلون؟"),
      ("3-10","mechanism","irritation from dry surface signals the gland to make more tears","السطح الناشف يتهيج، فالجسم يطلع دموع أكثر."),
      ("10-17","scope","dryness is one of the most common causes; blocked drainage is another","الجفاف من أشهر الأسباب، والتصريف المسدود سبب ثاني."),
      ("17-22","action","if tearing persists, an exam sorts out the cause","إذا يستمر الدمع، الفحص يحدد السبب."),
      ("22-25","close","","ما نخمّن، نفحص.")],
     [C("Dry eye can cause excess tears because irritated eyes make more tears","S91","your eyes make more tears when they are irritated by dry eye","AAO 2025; adults"),
      C("Dry eyes are one of the most common causes of excessive tearing","S93","This is one of the most common causes of excessive tearing","StatPearls",in_hook=False)],
     "Last line short (4 words) but carries the action","مرجح"),
   F("B","ليش الدمعة تحتاج طبقة دهنية؟","Why does a tear need an oily layer?","M05","tear-film-oil","oil-slows-evaporation",
     "What does oil do in a tear?","frame","Three-layer tear animation with the oil layer glowing","Oil layer role","One layer explained",
     [("0-3","hook","","ليش الدمعة تحتاج طبقة دهنية؟"),
      ("3-10","layers","tears have oily, watery and mucus layers","الدمعة ٣ طبقات: دهنية ومائية ومخاطية."),
      ("10-18","oil role","the outer oil layer keeps tears from drying up too quickly","الدهنية تمنع الدمعة تنشف بسرعة."),
      ("18-23","where it comes from","meibomian glands in the eyelids","تطلع من غدد بالجفن."),
      ("23-25","close","","الدمعة أذكى مما نتصور.")],
     [C("The oily layer keeps tears from drying up too quickly","S91","keeps tears from drying up too quickly","AAO 2025 explainer")],
     "Closing line is rhetorical","مرجح"),
   F("C","الدمعة الزايدة لها أكثر من سبب: إنتاج أكثر… أو تصريف أقل.","Excess tears have more than one cause: more production or less drainage.","M05","production-vs-drainage","two-ways-to-overflow",
     "Which is it?","frame","Sink analogy: tap on vs drain blocked (labelled analogy)","Overflow causes","Two broad mechanisms",
     [("0-4","hook","","الدمعة الزايدة لها أكثر من سبب: إنتاج أكثر… أو تصريف أقل."),
      ("4-12","tap","too much production, e.g. reflex tearing","إنتاج زايد، مثل الدمع الانعكاسي."),
      ("12-19","drain","outflow obstruction","أو مجرى مسدود."),
      ("19-23","action","persistent cases need evaluation","الحالة المستمرة تحتاج فحص."),
      ("23-25","close","","والفحص يفرّق بينهم.")],
     [C("Tear overflow is most often outflow obstruction or dryness-triggered excess","S92","most tear overflow is either due to outflow obstruction","AAO Q&A 2014; also poor distribution (StatPearls S93)")],
     "Source ranks obstruction first for overflow, dryness for reflex tearing; not a ranking for the viewer","مرجح")]),
]

# ---------------------------------------------------------------------------------------------
# Lint-driven corrections to the FIRST v1.1 draft (see LINT_FIRST_DRAFT.txt: 48 errors).
# The first draft was written by the author following the new rules; the linter then found mechanism duplicates,
# empty/short beats, a fear verb, an unsupported number and single-shape sets that the author had not noticed.
# ---------------------------------------------------------------------------------------------
def _fin(bid, fid):
    return next(f for b in BRIEFS if b["id"] == bid for f in b["fin"] if f["id"] == fid)
def _set(bid, fid, **kw):
    _fin(bid, fid).update(kw)
def _beat(bid, fid, idx, **kw):
    f = _fin(bid, fid); t, p, n, s = f["beats"][idx]
    n = kw.get("new_info", n); s = kw.get("spoken", s); p = kw.get("purpose", p)
    f["beats"][idx] = (t, p, n, s)

# hook beats: the new information of the hook beat is the question it poses and how the frame carries it
for _b in BRIEFS:
    for _f in _b["fin"]:
        _f["beats"] = [(t, p, (f"poses the question: {_f['gap']} (carried by {_f['carrier']})" if (n == "" and p.startswith("hook")) else n), s) for t, p, n, s in _f["beats"]]

# B01: mechanism dup (B,C both M04); fear verb 'يخرّب'; all-question set
_set("B01", "B", mech="M05")
_set("B01", "C", mech="M16", hook="نفس الثقب يحسّن النظر عند ناس، ويخليه أسوأ عند ناس آخرين.", gloss="The same pinhole improves sight for some people and makes it worse for others.", carrier="text",
     gap="Why does the same hole help some people and not others?", frame="Clinician-style hand holding a pinhole occluder in front of an eye-chart line, then a second line that does not improve; on-screen text `ليش؟`")
_beat("B01", "C", 0, spoken="نفس الثقب يحسّن النظر عند ناس، ويخليه أسوأ عند ناس آخرين.")
# B03: MSA words
_set("B03", "A", hook="شلون تسوي تجربة على نظارة الضوء الأزرق… واللابس يعرف إنها الحقيقية؟")
_beat("B03", "A", 0, spoken="شلون تسوي تجربة على نظارة الضوء الأزرق… واللابس يعرف إنها الحقيقية؟")
_set("B03", "C", hook="الضوء الأزرق من شاشتك يضر شبكيتك؟ الدليل لحد هسه ما يقول هيچ.")
_beat("B03", "C", 0, spoken="الضوء الأزرق من شاشتك يضر شبكيتك؟ الدليل لحد هسه ما يقول هيچ.")
_beat("B03", "B", 4, new_info="a realistic nightly plan the viewer can try tonight", spoken="جرّب الليلة تبعد الشاشة، وشوف نومك.")
# B05/B07/B08/B13: mechanism duplicates relabelled to the mechanism actually used
_set("B05", "C", mech="M08")
_set("B07", "A", mech="M18", hook="لوحات الألوان تكشف ٩٦٪ بس من الحالات… والباقي؟", gloss="Colour plates detect only about 96% of cases... and the rest?", gap="Who do plates miss, and why?")
_beat("B07", "A", 0, spoken="لوحات الألوان تكشف ٩٦٪ بس من الحالات… والباقي؟")
_beat("B07", "B", 4, new_info="complete colour loss exists but is rare", spoken="والنوع الكامل نادر، والفحص يحدد نوعك.")
_set("B08", "B", mech="M03", hook="حتى القيلولة بالعدسة تزيد الخطر — مو بس النوم الليلي.", gloss="Even a nap in your lenses raises the risk - not only overnight sleep.")
_beat("B08", "B", 0, spoken="حتى القيلولة بالعدسة تزيد الخطر — مو بس النوم الليلي.")
_set("B13", "C", mech="M16")
# B09 / B10: all-question sets -> make one a statement
_set("B09", "A", hook="إذا تبعّد الموبايل حتى تقرأ، غالباً هذا عمر… والحل بسيط.", gloss="If you hold your phone away to read, it's probably age - and the fix is simple.")
_beat("B09", "A", 0, spoken="إذا تبعّد الموبايل حتى تقرأ، غالباً هذا عمر… والحل بسيط.")
_set("B10", "B", hook="بفحص الاستجماتزم، الفرق بين \"واحد\" و\"اثنين\" أكبر مما تحس.", gloss="In astigmatism testing the difference between 'one' and 'two' is bigger than you feel.", carrier="text",
     frame="Handheld Jackson cross-cylinder flipping in front of a lens; on-screen text `ليش؟`")
_beat("B10", "B", 0, spoken="بفحص الاستجماتزم، الفرق بين \"واحد\" و\"اثنين\" أكبر مما تحس.")
_beat("B10", "A", 4, new_info="the viewer's job is an honest comparison and 'about the same' is a valid answer", spoken="جاوب بصدق، والباقي على الفاحص.")
# closings and empty beats
_beat("B11", "B", 4, new_info="a child who sits close to the TV is worth an eye exam", spoken="والطفل اللي يگعد گريب، فحصه يطمّنك أو يلگى الحل.")
_beat("B11", "C", 4, new_info="early detection protects school and sport performance", spoken="فحص طفلك الشامل يلگى المشكلة بدري.")
_beat("B12", "C", 4, new_info="protect eyes and surrounding skin together", spoken="احمي عيونك وجلدك سوا بنظارة UV وقبعة.")
_beat("B13", "A", 4, new_info="the exam, not guessing, finds the cause", spoken="ما نخمّن السبب، الفحص هو اللي يحدده.")
_beat("B13", "B", 4, new_info="the tear film is more structured than a drop of water", spoken="الدمعة أعقد بكثير من قطرة ماي.")
_beat("B13", "C", 2, new_info="outflow obstruction: the drainage channel is blocked so tears overflow")
_beat("B13", "C", 4, new_info="an exam separates production from drainage problems", spoken="الفحص هو اللي يفرّق بين المشكلتين.")

# ---------------------------------------------------------------------------------------------
# ITERATION 2: corrections after the adversarial review of the iteration-1 outputs (review/review_v11_iter1.py).
# Each item names the defect the human-style review found that the linter could not.
# ---------------------------------------------------------------------------------------------
# B01-B: hook assumed the viewer knew the clinical pinhole (not standalone)
_set("B01", "B", hook="تصغّر ثقب الورقة تشوف أحدّ… وتصغّره أكثر يصير أسوأ. ليش؟", gloss="Make the hole smaller and you see sharper... smaller still and it gets worse. Why?")
_beat("B01", "B", 0, spoken="تصغّر ثقب الورقة تشوف أحدّ… وتصغّره أكثر يصير أسوأ. ليش؟")
# B02-B: self-counting blinks changes blinking (observer effect) -> count someone else, present as informal
_set("B02", "B", hook="طالع بوجه واحد يتفرج ريلز دقيقة… وعدّ كم مرة يرمش.", gloss="Watch someone scroll reels for a minute and count how often they blink.",
     frame="Close-up of a friend scrolling; blink counter overlay starting at 0")
_beat("B02", "B", 0, spoken="طالع بوجه واحد يتفرج ريلز دقيقة… وعدّ كم مرة يرمش.")
_beat("B02", "B", 3, new_info="counting is informal: attending to your own blinking changes it, and this is not a measurement", spoken="هذا مو قياس دقيق، بس يعطيك فكرة ليش تحرگ.")
# B02-C: payoff needs efficacy research that has not been done
_set("B02", "C", payoff_ready=False)
# B03-C: the hook states the answer; unsourced comparison removed from the last beat
_set("B03", "C", aih=True, b2="If lab studies showed damage, why don't they apply to screens?")
_beat("B03", "C", 4, new_info="AAO links overexposure to sun blue/UV light to eye-disease risk", spoken="الأكاديمية تربط التعرض الزايد لضوء الشمس بأمراض العين.")
_fin("B03", "C")["claims"][1] = ("Overexposure to blue light and UV from the sun can raise eye-disease risk", "S32", "verified", "assertion", False,
     "overexposure to blue light and UV light rays from the sun can raise the risk of eye disease", "AAO Dec 2025; sun exposure")
# B06-B: 'in the middle of your vision' was wrong (the blind spot lies off-centre)
_set("B06", "B", hook="بكل عين اكو بقعة بدون خلايا مستقبلة… ليش ما تشوفها؟", gloss="Each eye has a patch without receptors... why don't you see it?")
_beat("B06", "B", 0, spoken="بكل عين اكو بقعة بدون خلايا مستقبلة… ليش ما تشوفها؟")
_fin("B06", "B")["claims"][0] = ("The blind spot is a retinal region devoid of photoreceptors", "S69", "verified", "assertion", True, "a retinal region devoid of photoreceptors", "Anstis 2010 primer")
# B08-B: 'napping' is a category shift from 'occasional overnight use'
_set("B08", "B", hook="حتى النوم النادر بالعدسة — مو بس العادة — يرفع الخطر.", gloss="Even rare sleeping in lenses - not only the habit - raises the risk.",
     frame="Person getting into bed with lenses still in; text `مرة وحدة؟`")
_beat("B08", "B", 0, spoken="حتى النوم النادر بالعدسة — مو بس العادة — يرفع الخطر.")
# B12-A: no comparator is stated by the source -> remove it from the hook
_set("B12", "A", hook="نظارة شمس غامقة بدون فلتر UV… شنو ممكن يصير ببؤبؤك؟", gloss="Dark sunglasses without a UV filter - what may happen to your pupil?",
     gap="What happens to the pupil behind dark lenses with no UV filter?")
_beat("B12", "A", 0, spoken="نظارة شمس غامقة بدون فلتر UV… شنو ممكن يصير ببؤبؤك؟")
_fin("B12", "A")["claims"][0] = ("Without a UV filter, pupils may stay larger behind dark lenses, letting more unfiltered UV enter", "S87", "verified", "assertion", True,
     "because your pupils may remain larger, thus allowing more unfiltered UV rays to enter", "AAO Q&A 2021; single ophthalmologist answer; 'may'")
# B13-A: hedged cause-naming for the viewer's own symptom -> general third-person statement
_set("B13", "A", hook="الدموع الزايدة مرات سببها جفاف. شلون يصير هيچ؟", gloss="Excess tears sometimes come from dryness. How does that happen?")
_beat("B13", "A", 0, spoken="الدموع الزايدة مرات سببها جفاف. شلون يصير هيچ؟")
_fin("B13", "A")["claims"][0] = ("Dry eyes are one of the most common causes of excessive tearing", "S93", "verified", "assertion", True, "This is one of the most common causes of excessive tearing", "StatPearls; adults; reflex tearing")
