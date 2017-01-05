# Converted to a python Slack bot by Mensly
#
# Original source by Joe Sabia and Aaron Rasmussen
# http://theofficestaremachine.com/

emotionToKey = {}
keyToVideo = {}

emotionToKey["1999"] = "1999"
emotionToKey["amused"] = "amused"
emotionToKey["charmed"] = "amused"
emotionToKey["cheery"] = "amused"
emotionToKey["diverted"] = "amused"
emotionToKey["employed"] = "amused"
emotionToKey["engaged"] = "amused"
emotionToKey["engrossed"] = "amused"
emotionToKey["entertained"] = "amused"
emotionToKey["tickled"] = "amused"
emotionToKey["amusing"] = "amused"
emotionToKey["diverted"] = "amused"
emotionToKey["cheery"] = "amused"
emotionToKey["engaged"] = "amused"
emotionToKey["employed"] = "amused"
emotionToKey["entertained"] = "amused"
emotionToKey["engrossed"] = "amused"
emotionToKey["entertained"] = "amused"
emotionToKey["cheery"] = "amused"
emotionToKey["diverted"] = "amused"
emotionToKey["employed"] = "amused"
emotionToKey["laughing"] = "amused"
emotionToKey["laughter"] = "amused"
emotionToKey["shame"] = "embarrassed"
emotionToKey["shameful"] = "embarrassed"
emotionToKey["awkward"] = "embarrassed"
emotionToKey["uncomfortable"] = "embarrassed"
emotionToKey["grumpy"] = "angry"
emotionToKey["acrimonious"] = "angry"
emotionToKey["apoplectic"] = "angry"
emotionToKey["infuriated"] = "angry"
emotionToKey["frustrated"] = "angry"
emotionToKey["frustration"] = "angry"
emotionToKey["bad-tempered"] = "angry"
emotionToKey["bitter"] = "angry"
emotionToKey["choleric"] = "angry"
emotionToKey["cross"] = "angry"
emotionToKey["enraged"] = "angry"
emotionToKey["fuming"] = "angry"
emotionToKey["furious"] = "angry"
emotionToKey["heated"] = "angry"
emotionToKey["ill-natured"] = "angry"
emotionToKey["ill-tempered"] = "angry"
emotionToKey["incensed"] = "angry"
emotionToKey["indignant"] = "angry"
emotionToKey["infurious"] = "angry"
emotionToKey["irate"] = "angry"
emotionToKey["livid"] = "angry"
emotionToKey["mad"] = "angry"
emotionToKey["outraged"] = "angry"
emotionToKey["passionate"] = "angry"
emotionToKey["pissed"] = "angry"
emotionToKey["aggressive"] = "angry"
emotionToKey["raging"] = "angry"
emotionToKey["seething"] = "angry"
emotionToKey["sore"] = "angry"
emotionToKey["steamed"] = "angry"
emotionToKey["stormy"] = "angry"
emotionToKey["vexed"] = "angry"
emotionToKey["wrathful"] = "angry"
emotionToKey["angry"] = "angry"
emotionToKey["mean"] = "angry"
emotionToKey["deadly"] = "angry"
emotionToKey["scary"] = "angry"
emotionToKey["murderous"] = "angry"
emotionToKey["anger"] = "angry"
emotionToKey["homicidal"] = "crazy"
emotionToKey["intense"] = "crazy"
emotionToKey["cranky"] = "annoyed"
emotionToKey["sassy"] = "annoyed"
emotionToKey["aggravated"] = "annoyed"
emotionToKey["antagonized"] = "annoyed"
emotionToKey["attacked"] = "annoyed"
emotionToKey["bugged"] = "annoyed"
emotionToKey["chagrined"] = "annoyed"
emotionToKey["disgruntled"] = "annoyed"
emotionToKey["displeased"] = "annoyed"
emotionToKey["exasperated"] = "annoyed"
emotionToKey["frosty"] = "annoyed"
emotionToKey["galled"] = "annoyed"
emotionToKey["irked"] = "annoyed"
emotionToKey["irritated"] = "annoyed"
emotionToKey["miffed"] = "annoyed"
emotionToKey["nerved"] = "annoyed"
emotionToKey["gruntled"] = "gruntled"
emotionToKey["nettled"] = "annoyed"
emotionToKey["peeved"] = "annoyed"
emotionToKey["piqued"] = "annoyed"
emotionToKey["sarcastic"] = "annoyed"
emotionToKey["riled"] = "annoyed"
emotionToKey["sore"] = "annoyed"
emotionToKey["ticked"] = "annoyed"
emotionToKey["unnerved"] = "annoyed"
emotionToKey["annoyed"] = "annoyed"
emotionToKey["disinterested"] = "bored"
emotionToKey["dull"] = "bored"
emotionToKey["stultified"] = "bored"
emotionToKey["stupefied"] = "bored"
emotionToKey["tedious"] = "bored"
emotionToKey["uninterested"] = "bored"
emotionToKey["bored"] = "bored"
emotionToKey["ambivalent"] = "bored"
emotionToKey["ennui"] = "bored"
emotionToKey["confident"] = "confident"
emotionToKey["arrogant"] = "confident"
emotionToKey["assertive"] = "confident"
emotionToKey["assured"] = "confident"
emotionToKey["certain"] = "confident"
emotionToKey["committed"] = "confident"
emotionToKey["convinced"] = "confident"
emotionToKey["coolheaded"] = "confident"
emotionToKey["determined"] = "confident"
emotionToKey["hopeful"] = "confident"
emotionToKey["imperturbable"] = "confident"
emotionToKey["levelheaded"] = "confident"
emotionToKey["optimistic"] = "confident"
emotionToKey["persuaded"] = "confident"
emotionToKey["poised"] = "confident"
emotionToKey["positive"] = "confident"
emotionToKey["positive"] = "confident"
emotionToKey["resolute"] = "confident"
emotionToKey["sanguine"] = "confident"
emotionToKey["satisfied"] = "confident"
emotionToKey["self-assured"] = "confident"
emotionToKey["self-confident"] = "confident"
emotionToKey["self-possessed"] = "confident"
emotionToKey["self-reliant"] = "confident"
emotionToKey["unperturbed"] = "confident"
emotionToKey["unruffled"] = "confident"
emotionToKey["addled"] = "confused"
emotionToKey["befuddled"] = "confused"
emotionToKey["bewildered"] = "confused"
emotionToKey["bemused"] = "confused"
emotionToKey["blurred"] = "confused"
emotionToKey["confounded"] = "confused"
emotionToKey["demented"] = "confused"
emotionToKey["dim"] = "confused"
emotionToKey["disorientated"] = "confused"
emotionToKey["disoriented"] = "confused"
emotionToKey["hazy"] = "confused"
emotionToKey["imprecise"] = "confused"
emotionToKey["indistinct"] = "confused"
emotionToKey["muddled"] = "confused"
emotionToKey["mystified"] = "confused"
emotionToKey["nonplussed"] = "confused"
emotionToKey["senile"] = "confused"
emotionToKey["shadowy"] = "confused"
emotionToKey["sketchy"] = "confused"
emotionToKey["unbalanced"] = "confused"
emotionToKey["unclear"] = "confused"
emotionToKey["unhinged"] = "confused"
emotionToKey["vague"] = "confused"
emotionToKey["woolly"] = "confused"
emotionToKey["confused"] = "confused"
emotionToKey["perplexed"] = "confused"
emotionToKey["perplexing"] = "confused"
emotionToKey["crazy"] = "crazy"
emotionToKey["insane"] = "crazy"
emotionToKey["dangerous"] = "crazy"
emotionToKey["creepy"] = "creepy"
emotionToKey["weird"] = "creepy"
emotionToKey["acquiescent"] = "defeated"
emotionToKey["compliant"] = "defeated"
emotionToKey["regretful"] = "defeated"
emotionToKey["regret"] = "defeated"
emotionToKey["dismissed"] = "defeated"
emotionToKey["fatalistic"] = "defeated"
emotionToKey["forbearing"] = "defeated"
emotionToKey["passive"] = "defeated"
emotionToKey["patient"] = "defeated"
emotionToKey["philosophical"] = "defeated"
emotionToKey["rejected"] = "defeated"
emotionToKey["resigned"] = "defeated"
emotionToKey["stoical"] = "defeated"
emotionToKey["submissive"] = "defeated"
emotionToKey["uncomplaining"] = "defeated"
emotionToKey["defeated"] = "defeated"
emotionToKey["drunk"] = "drunk"
emotionToKey["evil"] = "evil"
emotionToKey["demonic"] = "evil"
emotionToKey["satanic"] = "evil"
emotionToKey["devilish"] = "evil"
emotionToKey["diabolical"] = "evil"
emotionToKey["underhanded"] = "devious"
emotionToKey["deceitful"] = "devious"
emotionToKey["dishonest"] = "devious"
emotionToKey["dishonorable"] = "devious"
emotionToKey["unethical"] = "devious"
emotionToKey["unprincipled"] = "devious"
emotionToKey["immoral"] = "devious"
emotionToKey["unscrupulous"] = "devious"
emotionToKey["fraudulent"] = "devious"
emotionToKey["dubious"] = "devious"
emotionToKey["unfair"] = "devious"
emotionToKey["treacherous"] = "devious"
emotionToKey["duplicitous"] = "devious"
emotionToKey["crafty"] = "devious"
emotionToKey["cunning"] = "devious"
emotionToKey["calculating"] = "devious"
emotionToKey["artful"] = "devious"
emotionToKey["conniving"] = "devious"
emotionToKey["scheming"] = "devious"
emotionToKey["sly"] = "devious"
emotionToKey["wily"] = "devious"
emotionToKey["sneaky"] = "devious"
emotionToKey["furtive"] = "devious"
emotionToKey["secretive"] = "devious"
emotionToKey["clandestine"] = "devious"
emotionToKey["surreptitious"] = "devious"
emotionToKey["covert"] = "devious"
emotionToKey["snide"] = "devious"
emotionToKey["crooked"] = "devious"
emotionToKey["shady"] = "devious"
emotionToKey["dirty"] = "devious"
emotionToKey["devious"] = "devious"
emotionToKey["icy"] = "devious"
emotionToKey["appalled"] = "disgusted"
emotionToKey["horrified"] = "disgusted"
emotionToKey["nauseating"] = "disgusted"
emotionToKey["offensive"] = "disgusted"
emotionToKey["offended"] = "disgusted"
emotionToKey["repellent"] = "disgusted"
emotionToKey["repulsive"] = "disgusted"
emotionToKey["scandalized"] = "disgusted"
emotionToKey["shocking"] = "disgusted"
emotionToKey["sick"] = "disgusted"
emotionToKey["sickening"] = "disgusted"
emotionToKey["contempt"] = "disgusted"
emotionToKey["disgusted"] = "disgusted"
emotionToKey["abashed"] = "embarrassed"
emotionToKey["ashamed"] = "embarrassed"
emotionToKey["discomposed"] = "embarrassed"
emotionToKey["bashful"] = "embarrassed"
emotionToKey["blushing"] = "embarrassed"
emotionToKey["chagrined"] = "embarrassed"
emotionToKey["discomfited"] = "embarrassed"
emotionToKey["discomposed"] = "embarrassed"
emotionToKey["disconcerted"] = "embarrassed"
emotionToKey["flustered"] = "embarrassed"
emotionToKey["humiliated"] = "embarrassed"
emotionToKey["mortified"] = "embarrassed"
emotionToKey["self-conscious"] = "embarrassed"
emotionToKey["shamed"] = "embarrassed"
emotionToKey["shamefaced"] = "embarrassed"
emotionToKey["sheepish"] = "embarrassed"
emotionToKey["shy"] = "embarrassed"
emotionToKey["shy"] = "embarrassed"
emotionToKey["tongue-tied"] = "embarrassed"
emotionToKey["embarrassed"] = "embarrassed"
emotionToKey["sensitive"] = "embarrassed"
emotionToKey["embarassed"] = "embarrassed"
emotionToKey["funny"] = "funny"
emotionToKey["silly"] = "funny"
emotionToKey["hilarious"] = "funny"
emotionToKey["goofy"] = "funny"
emotionToKey["ridiculous"] = "funny"
emotionToKey["guilty"] = "guilty"
emotionToKey["excited"] = "crazy"
emotionToKey["stoked"] = "crazy"
emotionToKey["excitable"] = "crazy"
emotionToKey["extreme"] = "crazy"
emotionToKey["ebullient"] = "happy"
emotionToKey["beaming"] = "happy"
emotionToKey["beatific"] = "happy"
emotionToKey["blissful"] = "happy"
emotionToKey["blithe"] = "happy"
emotionToKey["buoyant"] = "happy"
emotionToKey["carefree"] = "happy"
emotionToKey["cheerful"] = "happy"
emotionToKey["cheery"] = "happy"
emotionToKey["chirpy"] = "happy"
emotionToKey["contented"] = "happy"
emotionToKey["love"] = "happy"
emotionToKey["loving"] = "happy"
emotionToKey["delighted"] = "happy"
emotionToKey["ecstatic"] = "happy"
emotionToKey["elated"] = "happy"
emotionToKey["euphoric"] = "happy"
emotionToKey["exhilarated"] = "happy"
emotionToKey["exultant"] = "happy"
emotionToKey["gleeful"] = "happy"
emotionToKey["gratified"] = "happy"
emotionToKey["grinning"] = "happy"
emotionToKey["jocular"] = "happy"
emotionToKey["jocund"] = "happy"
emotionToKey["jolly"] = "happy"
emotionToKey["jovial"] = "happy"
emotionToKey["joyful"] = "happy"
emotionToKey["joyous"] = "happy"
emotionToKey["jubilant"] = "happy"
emotionToKey["lighthearted"] = "happy"
emotionToKey["merry"] = "happy"
emotionToKey["overjoyed"] = "happy"
emotionToKey["radiant"] = "happy"
emotionToKey["rapturous"] = "happy"
emotionToKey["satisfied"] = "happy"
emotionToKey["smiling"] = "happy"
emotionToKey["sunny"] = "happy"
emotionToKey["thrilled"] = "happy"
emotionToKey["untroubled"] = "happy"
emotionToKey["happy"] = "happy"
emotionToKey["horny"] = "horny"
emotionToKey["seductive"] = "horny"
emotionToKey["aroused"] = "horny"
emotionToKey["sexy"] = "horny"
emotionToKey["flirty"] = "horny"
emotionToKey["sexual"] = "horny"
emotionToKey["sultry"] = "horny"
emotionToKey["lovey"] = "horny"
emotionToKey["romantic"] = "horny"
emotionToKey["starving"] = "hungry"
emotionToKey["hangry"] = "hungry"
emotionToKey["hungry"] = "hungry"
emotionToKey["absorbing"] = "intrigued"
emotionToKey["appealing"] = "intrigued"
emotionToKey["arousing"] = "intrigued"
emotionToKey["captivated"] = "intrigued"
emotionToKey["compelling"] = "intrigued"
emotionToKey["curious"] = "intrigued"
emotionToKey["enchanted"] = "intrigued"
emotionToKey["engaged"] = "intrigued"
emotionToKey["enthralled"] = "intrigued"
emotionToKey["fascinated"] = "intrigued"
emotionToKey["gripping"] = "intrigued"
emotionToKey["interested"] = "intrigued"
emotionToKey["piquing"] = "intrigued"
emotionToKey["riveting"] = "intrigued"
emotionToKey["intrigued"] = "intrigued"
emotionToKey["jealous"] = "jealous"
emotionToKey["envious"] = "jealous"
emotionToKey["smug"] = "proud"
emotionToKey["content"] = "proud"
emotionToKey["contented"] = "proud"
emotionToKey["glad"] = "proud"
emotionToKey["satisfied"] = "proud"
emotionToKey["thankful"] = "proud"
emotionToKey["pleased"] = "proud"
emotionToKey["sardonic"] = "proud"
emotionToKey["complacent"] = "proud"
emotionToKey["proud"] = "proud"
emotionToKey["grateful"] = "relieved"
emotionToKey["reassured"] = "relieved"
emotionToKey["reassuring"] = "relieved"
emotionToKey["thankful"] = "relieved"
emotionToKey["relieved"] = "relieved"
emotionToKey["lonely"] = "sad"
emotionToKey["hurt"] = "sad"
emotionToKey["disappointed"] = "sad"
emotionToKey["sentimental"] = "sad"
emotionToKey["sappy"] = "sad"
emotionToKey["bummed"] = "sad"
emotionToKey["awful"] = "sad"
emotionToKey["blah"] = "sad"
emotionToKey["blue"] = "sad"
emotionToKey["crestfallen"] = "sad"
emotionToKey["dejected"] = "sad"
emotionToKey["depressed"] = "sad"
emotionToKey["desolate"] = "sad"
emotionToKey["despairing"] = "sad"
emotionToKey["despondent"] = "sad"
emotionToKey["disconsolate"] = "sad"
emotionToKey["dismal"] = "sad"
emotionToKey["doleful"] = "sad"
emotionToKey["down"] = "sad"
emotionToKey["downcast"] = "sad"
emotionToKey["forlorn"] = "sad"
emotionToKey["gloomy"] = "sad"
emotionToKey["glum"] = "sad"
emotionToKey["harrowing"] = "sad"
emotionToKey["heartbreaking"] = "sad"
emotionToKey["heartbroken"] = "sad"
emotionToKey["heartrending"] = "sad"
emotionToKey["inconsolable"] = "sad"
emotionToKey["melancholy"] = "sad"
emotionToKey["miserable"] = "sad"
emotionToKey["miserable"] = "sad"
emotionToKey["mournful"] = "sad"
emotionToKey["pathetic"] = "sad"
emotionToKey["pitiful"] = "sad"
emotionToKey["sorrowful"] = "sad"
emotionToKey["sorry"] = "sad"
emotionToKey["tragic"] = "sad"
emotionToKey["traumatic"] = "sad"
emotionToKey["unfortunate"] = "sad"
emotionToKey["unhappy"] = "sad"
emotionToKey["unhappy"] = "sad"
emotionToKey["woebegone"] = "sad"
emotionToKey["wretched"] = "sad"
emotionToKey["sad"] = "sad"
emotionToKey["deep"] = "deadpan"
emotionToKey["contemplative"] = "serious"
emotionToKey["deep"] = "serious"
emotionToKey["apathetic"] = "serious"
emotionToKey["callous"] = "serious"
emotionToKey["cold"] = "serious"
emotionToKey["cool"] = "serious"
emotionToKey["dour"] = "serious"
emotionToKey["earnest"] = "serious"
emotionToKey["earnest"] = "serious"
emotionToKey["emotionless"] = "serious"
emotionToKey["frigid"] = "serious"
emotionToKey["genuine"] = "serious"
emotionToKey["constipated"] = "serious"
emotionToKey["grave"] = "serious"
emotionToKey["grim"] = "serious"
emotionToKey["humorless"] = "serious"
emotionToKey["impassive"] = "serious"
emotionToKey["passionless"] = "serious"
emotionToKey["pensive"] = "pensive"
emotionToKey["quixotic"] = "pensive"
emotionToKey["perfunctory"] = "serious"
emotionToKey["phlegmatic"] = "serious"
emotionToKey["poker-faced"] = "serious"
emotionToKey["reserved"] = "serious"
emotionToKey["restrained"] = "serious"
emotionToKey["sincere"] = "serious"
emotionToKey["sober"] = "serious"
emotionToKey["solemn"] = "serious"
emotionToKey["somber"] = "serious"
emotionToKey["stern"] = "serious"
emotionToKey["stoic"] = "serious"
emotionToKey["stoical"] = "serious"
emotionToKey["stony-faced"] = "serious"
emotionToKey["thoughtful"] = "pensive"
emotionToKey["undemonstrative"] = "serious"
emotionToKey["unemotional"] = "serious"
emotionToKey["unexcitable"] = "serious"
emotionToKey["unfeeling"] = "serious"
emotionToKey["unsentimental"] = "serious"
emotionToKey["unsmiling"] = "serious"
emotionToKey["wholehearted"] = "serious"
emotionToKey["serious"] = "serious"
emotionToKey["amazed"] = "serious"
emotionToKey["blank"] = "serious"
emotionToKey["indifferent"] = "serious"
emotionToKey["stupid"] = "stupid"
emotionToKey["dumb"] = "stupid"
emotionToKey["suprised"] = "surprised"
emotionToKey["astonished"] = "surprised"
emotionToKey["astounded"] = "surprised"
emotionToKey["incredulous"] = "surprised"
emotionToKey["flabbergasted"] = "surprised"
emotionToKey["dazed"] = "surprised"
emotionToKey["dumbfounded"] = "surprised"
emotionToKey["dumbstruck"] = "surprised"
emotionToKey["floored"] = "surprised"
emotionToKey["flummoxed"] = "surprised"
emotionToKey["shaken"] = "surprised"
emotionToKey["shocked"] = "surprised"
emotionToKey["disbelieving"] = "surprised"
emotionToKey["speechless"] = "surprised"
emotionToKey["staggered"] = "surprised"
emotionToKey["startled"] = "surprised"
emotionToKey["stunned"] = "surprised"
emotionToKey["stupefied"] = "surprised"
emotionToKey["thunderstruck"] = "surprised"
emotionToKey["surprised"] = "surprised"
emotionToKey["lethargic"] = "confused"
emotionToKey["tired"] = "sad"
emotionToKey["lazy"] = "sad"
emotionToKey["jaded"] = "sad"
emotionToKey["bushed"] = "sad"
emotionToKey["dead"] = "sad"
emotionToKey["jaded"] = "sad"
emotionToKey["dog-tired"] = "sad"
emotionToKey["drained"] = "sad"
emotionToKey["enervated"] = "sad"
emotionToKey["exhausted"] = "sad"
emotionToKey["fatigued"] = "sad"
emotionToKey["jaded"] = "sad"
emotionToKey["sleepy"] = "sad"
emotionToKey["knackered"] = "sad"
emotionToKey["pooped"] = "sad"
emotionToKey["wasted"] = "sad"
emotionToKey["weary"] = "sad"
emotionToKey["zonked"] = "sad"
emotionToKey["crying"] = "sad"
emotionToKey["agitated"] = "worried"
emotionToKey["agonized"] = "worried"
emotionToKey["fearful"] = "worried"
emotionToKey["anxious"] = "worried"
emotionToKey["fear"] = "worried"
emotionToKey["bedeviled"] = "worried"
emotionToKey["bothered"] = "worried"
emotionToKey["brooding"] = "worried"
emotionToKey["concerned"] = "worried"
emotionToKey["disquieted"] = "worried"
emotionToKey["distressed"] = "worried"
emotionToKey["disturbed"] = "worried"
emotionToKey["flustered"] = "worried"
emotionToKey["fretted"] = "worried"
emotionToKey["nervous"] = "worried"
emotionToKey["panicked"] = "worried"
emotionToKey["perturbed"] = "worried"
emotionToKey["plagued"] = "worried"
emotionToKey["preoccupied"] = "worried"
emotionToKey["rattled"] = "worried"
emotionToKey["scared"] = "worried"
emotionToKey["terrified"] = "worried"
emotionToKey["afraid"] = "worried"
emotionToKey["stewed"] = "worried"
emotionToKey["stressed"] = "worried"
emotionToKey["taxing"] = "worried"
emotionToKey["tormented"] = "worried"
emotionToKey["tormented"] = "worried"
emotionToKey["troubled"] = "worried"
emotionToKey["unsettled"] = "worried"
emotionToKey["upset"] = "worried"
emotionToKey["worried"] = "worried"


keyToVideo['1999'] =  ("TA8oR4PUdZU",
"zgKY8adiM10",
"dKMj48VjgJM",
"u_PebIBQQko",
"TbVyBNIvmtE",
"rhS6GcPqqdc",
"M91QTTJ0kNw",
"w4Yzk8eaP7U",
"evZ4k49nFLs",
"a7j3GIfG3hU",
"j9qTqbTsRI4",
"mAtFy1bvVPY",
"y0dIhavzTKE",
"IuMyF9nPHxU",
"j7AH1AbFLKU",
"uowhjwuHUZw",
"hCsu0dn8huY",
"h-Dxjw_Xr-I",
"1pzgPet_LPs",
"D5EXe707K_E",
"0rrj3o-Xde0",
"cVj1QvLuM_I",
"hAzNtjNw8jE",
"NxHqh_F1qj4",
"yHAokMMEbJE",
"7cm8cOMwheo",
"905_6v6a4GY",
"L9CBq4Da7P4")

keyToVideo['amused'] =  ("thx77DeHLZY",
"aXHAos9M7_k",
"G9uwTUxh-0w",
"79UVgs0kn4c",
"RPUpPq6SSUo",
"23Xyt_zT_1A",
"VtHMMTpGf3k",
"LUFUUCtmAMM",
"dYBr2gK4XUM",
"Url9ju-dBKs",
"8aNSmz-bv2E",
"pi_q9xtV_DI",
"c0nY5RXq9Eo",
"fR2T2ksmWns",
"8UisCh8Cwcc",
"yUd3_tuA9AU",
"CXxlWRBHOZw",
"zPp-QvYtqGk",
"Sm5T2H4kEWU")

keyToVideo['angry'] =  ("93F60yL5kMw",
"o6eiebBdiD4",
"CgPqeyr8lAw",
"c0XBdJAzWKs",
"KR7NxAazbgE",
"McTaqIDuvUI",
"QCqZdRVxx1g",
"hgB2WqAxV9M",
"0cd8vQ2bKLE",
"UzA1dKuKfOM",
"pkM1ZzFhGss",
"Hr96_uT2DUk",
"GtXM5w7C9zE",
"4LnSzaAR_j8",
"kxeardnaBSQ",
"M0zMiU-FVpc",
"RjZ2gPvtX1Y",
"Mv-iMSBlmWo",
"gV27pkqg2_w",
"hozv-60KZJQ",
"-B5huqaFk0g",
"M9g4nCJCEYA",
"rOgqiOhZi3c",
"D07wIzt8gRo",
"mm_b5ctnKAc",
"zc_9mAtBYrQ",
"WONNrAQH8oY",
"wi5YGQRWCg8",
"M32r7p5yNOY",
"p1c_1dvKkXo",
"huOf7AQSzw4",
"Uz9CtXU7NBQ",
"FVLGpfl8ebI",
"aspT6yof-nM",
"E8WizAVMoFY",
"QRN-Hw6RXUc",
"3gU7a9ryTgE",
"oH6uipm9tLg",
"_R4nHKFlws0",
"XZrDoz5vnE0",
"JITiQQQG1dI",
"5XrQkhFHBfE",
"1ezokChVkJM",
"qu5UeuKtva4",
"Yw1nqZ3bFAQ",
"UdYHchZaCOE",
"GpSCwGtPdE8",
"-kF52BvA_Hw",
"8MznS0dz3uo",
"LL4QnbfH4aY",
"OB36BEkbGzs")

keyToVideo['annoyed'] = ("xp12AxZstak",
"gwo3ksZ6F24",
"v_AXKpIjlB8",
"BOvQuiRhEkc",
"xP8XwhecJdY",
"K-5SYpP6YMI",
"YLIBUL6v1ls",
"kGEhJ3kh3XM",
"TkWN_pOza3g",
"Oda_1YYNPug",
"AgGk91Vepug",
"KabNjbqogE4",
"IHqT_DE2TP0",
"fLVFrpxbaEY",
"muuEQMdKUx4",
"42B981N__nA",
"_ZY5594vxz0",
"anPJiVe7Anw",
"_erHjmOdWwA",
"-q5l-wkLs1U",
"wiylZ7GULMk",
"dVQdm-YC2k0",
"wMM9frM3ypU",
"ALkIpzTqn0s",
"iZr-RphuzaQ",
"6cMp_LGYf-g",
"GlJK-pE6iPc",
"TwtWgpSda3g",
"jafw9lt--zg",
"YsreAbcIlfk",
"HzmUHZI8id8",
"G6n7lg56vWc",
"eQhDZ-p-fu4",
"nFwWL8W62Vw",
"IrK-TeB-ZZA",
"s0C_rZZ0cto",
"N9OJG_DNCPA",
"zS206GgmpnM",
"hXUUXtlr6WY",
"sMji1Ru_P1A",
"ouZ6PM_wc0g",
"_AcpnD4CVXM",
"sEtPqgK8JOQ",
"wC6LnsKyzBE",
"HsSls2KriPA",
"s474knyt5MM",
"8JyS_6wwn00",
"BzvBaEZCi7A",
"FJQznDwg5M8",
"zC5drsjz3f8",
"iJMU6ZtFKLg",
"qtngXXRrJqs",
"09nfnsUlnH4")

keyToVideo['bored'] = ("KO45TUVjayA",
"ndmdheKX5h4",
"EZ6VwS7Z7nc",
"H8z48TYxIbc",
"3ifn0ecjJBM",
"je2b_qPSFRc",
"_Ufg_4h7IUQ",
"jBiPXD50T6c",
"oAA9G-crEhw",
"VmOxc5U_wQU",
"89BCmZnA6Yw",
"_e2AJ95VLh8",
"Vc-rc9QtQWI")

keyToVideo['gruntled'] = ("2joetGgluqc",
"2joetGgluqc")

keyToVideo['confident'] = ("zi_L9LE3l-U",
"giSCMyP7v7Q",
"BAoqXcdkjA0",
"xRXHY_U2HR8",
"d12YiM7Q7hg",
"2y1Ob-mpQg4",
"TAdDqJ2f6I4",
"Ri0itUgoQok",
"7jZ48uk_jAU",
"3OnOesYCLo4",
"ybXmxcgKz_w",
"P5Z8WXdwPJU",
"NSwn6eD5qjQ",
"CQYTl8EEgC4",
"E-m3Y_hpl1M")

keyToVideo['confused'] = ("vmnoUN2_3w8",
"1cm5CGS3W0M",
"4CbZNmLe2WI",
"Zt3ysKxRU7Q",
"RuFIuUWIzD0",
"CFQNUjPePWo",
"ayP_K4savLo",
"tiSl1YOkGnM",
"UcBxgs_ZUKk",
"oXR2FV5i9mY",
"NJ3AXs62Q9g",
"HGJeJEPQcTE",
"x1SDZwPznVU",
"Vwuk9iSPqbA",
"qR4hJ9XVKVY",
"t2gx-AQj0M0",
"EcOYTTZgvHg",
"KP0LQB7LmAY",
"R1Ach6zRJcM",
"Ra0ozoaG5pQ",
"vunsmJoJ6Jw",
"P1bfAYNQN5E",
"ancW33Hmf8Q",
"zvMLIeg1gb8",
"pWWAVijrK8M",
"P4XR9fIT4OA",
"byvID67jFpo",
"ffIEc5LWDvA",
"fMoUU79nPq4",
"TN1BzfJS9zQ",
"oU1EvtdnA3A",
"DPKqO12TUGM",
"E-PNhUi58LU",
"iNRxX1CqGGU",
"9cfWfPI155Y",
"iBt1RvTWazQ",
"l1PGfqiN6yQ",
"WpJ_fgs0poM",
"FKHo6Aes-Sg",
"QR8WatApzTo",
"rTT3LGj7O4A",
"4yolMWrBDCY",
"E1elbESzTmE",
"_4uUPZhXp24",
"SESeQoMXDBs",
"l8kj36fWO2c",
"JIyTCC6q794",
"VUdsKhKiTqE",
"50gh8imsc0w",
"qR-JyIXevXw",
"snGCaOBULD0",
"JxV7BhIFFWk",
"u2aLw8uJauY",
"AeAoebbtyRg",
"eEq7BcONyO0",
"RXoTtJw7Bgs",
"7rKHBAbsuYg",
"tY92_yGq_w8")

keyToVideo['crazy'] = ("Z_TSkPivPpg",
"NuHVr6GLhWo",
"_dw4kgWLV1I",
"3rvxCiazeHw")

keyToVideo['creepy'] = ("5mMRrkMmXjI",
"wSslbmoRpK4",
"h1ZEgnuGH2Q",
"5Ae8-Ehm1pU",
"kk1LcL7dZTc")

keyToVideo['defeated'] = ("0roSsayezn4",
"MFjIMLP18jI",
"p2rs4PdzB-U",
"tn6Iu1iRo_s",
"GKMSclij5Co",
"UKMuTnGSpuA",
"luPbNr5hsqg",
"qpuuwxA0U3M",
"fgHWLb-HAX4",
"KTFWuKwUcCM",
"5rIdveHa2MA",
"158ROL6GTIc",
"8RwmBUusHkA",
"kmO2-C11LFc",
"m_HhdBgdQo0",
"mCcqHb5f264",
"oYzf4j_sjCs",
"HkYlg8kob_w")

keyToVideo['devious'] = (
"zTIsDB35QQw",
"RK_ZbBa1vL4",
"FG1snl5Oqig",
"QVyJZfJWJKs",
"yioKhHtxH4A",
"l6E-7A9x3mM",
"P0690zodE7I",
"Wfjzfs1e-w0",
"4Jq31D1SzJ4",
"iJyW5J2xyyQ",
"EUgx-jL4MmA",
"m2NhFNncy8Q",
"7-jTPNSbbS0",
"8p4I692kPAk",
"m5C8kZIZfWU",
"-FDFEsKEE9M",
"xzHXnS8B4Mo",
"f4tGfaaV8Xw")

keyToVideo['disgusted'] = ("BV4h9JPbG2o",
"IfRCjXzBmhQ",
"WuFnfpYLD98",
"oA9itbRRzzY",
"QomNQ8FTkHw",
"nvzXfz5X2BU",
"B-WDQYNc4cc",
"KgWQZ58HjXg",
"U_cwkZ3CVXY",
"8wHF_EL1hrA",
"OLF-Ro9avYk",
"rYo3TgfiaBQ",
"l_1O7ukfcMw",
"96YDsC3Jcu4",
"odXVji3r664",
"SwTxkGPc2bo")

keyToVideo['drunk'] = ("I2EM9aucz6s",
"oWgDT9J-k5c",
"4XR-3kwaNKg")

keyToVideo['embarrassed'] = ("rPvBS1wR89I",
"5-7e3hYTvO4",
"IRyyiPgM-lk",
"uEjOXbmIg5E",
"7taKnePitmo",
"1fSL5izG4Dw",
"3QJMBFscQp8",
"0WGcNkscqTY",
"Cv_ydLc_Gwg",
"C6mjWVIT0OE",
"vRU5-V_V4BE",
"uhjd7ND_-zo",
"hoDxKJS-lNQ",
"5s5IfLyEX6M",
"NFm1kWEAhwY",
"ZcCqocZ4XfE",
"h62oXu6Y37o",
"6b2vQ6WOyhQ",
"IQoCFd-9BkU",
"MBL1bx1l1ak",
"lmzTt_qVxuQ",
"nenzBsPJBwM",
"JClRupmgaQs",
"vj6le64p_6U",
"OdL7Ugc2W1s",
"q6hYd_sO_VU",
"kmPmmbz8WB4",
"wf6yaYFlZSA",
"meyqL-zC3Zs",
"eB51iXc6-Vs",
"olLnI_4rKCQ",
"COK3__XWMFI",
"rb5LOimHw7w",
"0R1lFjsjZoI",
"HdlzU6d1EJw")

keyToVideo['evil'] = ("rPTABGn52-Q",
"rPTABGn52-Q",
"kYy36UbZ92o")

keyToVideo['funny'] = ("TJxwipvr9mc",
"gk2zutgRKkw",
"vYU3tCaah4A",
"bHI6AF4vZeY",
"G9uwTUxh-0w",
"VWxnT6ZsgxM",
"GRKPlbJXL7c",
"WpX5Emy4MV4",
"h-nniDUBdoc",
"5LQlrU30VLo",
"GiJ3-Nwr59M",
"WsXC3gBPcag")

keyToVideo['guilty'] = ("U2TvBfzEhVo",
"nJk8RcWG5_M")

keyToVideo['happy'] = ("w0XZDn94-Js",
"LizbGz29sRA",
"P3hW0d2ULgE",
"uGe7U35jSKc",
"HZKb4msYwFw",
"L-0FVWYlPMk",
"U4JvKiUynL4",
"GHHijXjJDaY",
"4csEmvZnLOY",
"ziJ5bdwSDQo",
"vDuuX7C1dGE",
"-xUMQ5rU2cc",
"kSUp7umeSDk",
"28PwM7w3WXQ",
"XD4VCJEA3a8",
"zPHa3lqWTUk",
"G63OV1-VYAY",
"_eaWxSYBvFA",
"JqejaNQ7jT4",
"4SgcbokhqjQ",
"7j1czpcuLVE",
"JlXsx_ZnKog",
"mmtWydOo_Gc",
"JgDvpgWgDoE",
"F5Eib4HnqEI",
"9NdgCMzhnCU",
"xq-9PIOgrfk",
"7i4WbMDDiSM",
"7bo1crsQwOQ",
"vRB_X9Q0iNk",
"PGDsAg_Xe0o",
"sPydy2jEbZM",
"T9jDdUU8GWo",
"CntvMLuuBLU",
"w8NqIfMiAYw",
"2Zx9m8XfMdU",
"9g6E46isCOM",
"xLfRdMYCRHE",
"-Jvx2BP3w4U",
"YGV_vvwNNU4",
"fzMR2v7R6hY",
"Aje1kNjuN1g",
"h_mCGBh3g8k",
"5dy1kIuAaXQ",
"k1Ccf5csFQc",
"gHqdupApIqw",
"XvEuI2bwdbA",
"YjPXPx1UL-4",
"da4X-7syMcc",
"Jor0XuO5ZEU",
"0jXiLp912ls",
"YJqWAq7l_Kw",
"hrSrVj352sM",
"KKk9A-6tOGs",
"_NjPY5oby0I",
"JqyT1OWeqgw",
"HdMYIS9gkbo",
"E5zRAFN72vA",
"tl9LO6pdvYg",
"MBl2_QjlzCU",
"FvNJksVmHz8",
"HKdsNyFyqDY",
"Ihs-pAmybv4",
"dgUGts_tmQM",
"ESmzMCM_mVI",
"UNPzbYncD3E",
"oXtHsNikcRM",
"GVIB6PH5VGU",
"Y95BvYXIKOw",
"s8tBVUZfby4",
"5c2rBJ5FmBE",
"NLpJnVEVI1g",
"iGbBzi_YWK0",
"YScAWwR2LPo",
"SoaY6Z507wo",
"OMOZES09kOU",
"RZ3CQsUvzAQ",
"Q79Y9WOYvzE",
"Nt1qsckuh_8",
"AqI3WgMI2Dk",
"1mf7DW77tno")

keyToVideo['horny'] = ("LbKdoJqJWy8",
"9zwun7ylOF8",
"gh1yk8kS8gI",
"lO8nfG3M3qw",
"CzOnWiNwA-4",
"P9rtnTi6UQ0",
"GzvUezVCAXw",
"y7kDLOZO6XM",
"7yqoR_k82k4",
"D4Vj-78YlTQ",
"UaQR__YcAEg")

keyToVideo['hungry'] = ("L08kScTCJ8E",
"emZG_EchST4",
"GRKPlbJXL7c",
"5qNdPYpdeis",
"UgtjZOuiP6g")

keyToVideo['intrigued'] = ("wRmIxCBJHyo",
"PLwKLVHpE4I",
"1pFW3awc8Rg",
"yjthEeKS-Mk",
"DNCIcPUibMw",
"0-SBh9JVWtU",
"gjGff2YZGHA",
"YCt9DD_q4gc",
"v2VOn7au-qs",
"reoPwQYWrgg",
"nXWpP9CqfB0",
"vuJgT7QQ-7w")

keyToVideo['jealous'] = ("5XrQkhFHBfE",
"SkvxeTVAOO0",
"zIutEXJ5j_g")




keyToVideo['pensive'] = ("mEGHM4UdBqM",
"usD2gZYuDc0")

keyToVideo['proud'] = ("ZEOThui7lRE",
"sj5LxLUcNRo",
"Q2rpCCXKCRw",
"JuuARSvekJ4",
"KC1PSSSdmzY",


"n77f4w3xGpU",
"5IICi3FOPDs",
"qXJ4gvIZ3ck",
"m8VVRCEtt4U",
"8m1UYp7BL3M",
"LSIaBRFYe9E",
"rolinrwWuM0",
"f9tpem-9ltU",
"TZEkjFKO9sk",
"76TZOKeY7bM",
"kbaYNgBmDcI",
"NIaQKOo7hUs",
"t794Kjr9H2M")

keyToVideo['relieved'] = ("wnLuUsFPCP4",
"Mxb87asgL7U",
"AZNdGkdoYz4",
"0GZfUowtocY",
"juzVN2vvjLs",
"2N46uRa-UBo",
"QiyHeqmOqHw",
"q9xWGVuhJa4",
"sOVMF4Dfb38",
"inB5BVMT_0E",
"o6f2K_3afOQ",
"fxsstAjTg4U")

keyToVideo['sad'] = ("eQSUrp-Ybu8",
"YLq5z-L-kcY",
"5rouugjlvvc",
"4ox4ACGcijk",
"93HIlq-ChXg",
"CxbnVWuo-RU",
"cJhyJQ4yf6A",
"Dl9rE6U8m6Y",
"qjdfjWS0UTg",
"yeOt57vFljk",
"YCvhiGvs_aU",
"RI1_ez7AN_0",
"7eNM0TFaB50",
"QlfQMYGJjKo",
"FQcRaFFQa-Q",
"l9VRollFeqw",
"p8Dr6rmTkfc",
"B1XfRoW5dJ8",
"0ml_ac1o7bw",
"5Y0tUSvRQVE",
"ptBtCTb3phI",
"_rsMR52vsnY",
"SFAgZP8P_l8",
"iVX4jDjbUSI",
"knCY1ziGiU4",
"YNaVhp0qIOk",
"JXykYQvm9rk",
"nWJ-fURekP8",
"i00gVG4VSWo",
"-9AZ3-Gdu34",
"MhxdbpCYpcQ",
"LM2nrWjmqp4",
"XXqnmq7V9Gs",
"J5HhqN1JHoU",
"p_Z6ybOaVeE",
"oiaE0CFMkSs",
"zemlhQe_oY0")

keyToVideo['serious'] =  ("wbobYVA2NEE",
"WNiwGblaQrE",
"Sq7U0H1bkpY",
"kmPdyqVUx04",
"oIKlCgIIK6s",
"hzo12QKNvLc",
"n_TBD2lM8fM",
"_yFtgw3EnU4",
"QiYfgV0ybrI",
"WTvyDCWy8AU",
"O76mmg5zzCM",
"zu8maJo7Obg",
"Vn26In11c30",
"l_x9-3ONtuY",
"ePrPFYKxMlE",
"CDv4mUOLa8Y",
"FR2CMpcpSmk",
"mEGHM4UdBqM",
"YsQBR641ANY",
"2rorJSiDiwY",
"LoOFcBTd43Y",
"EpE7_iT94fo",
"JO-wsYbIBfE",
"ZAu-jmYhBNE",
"hVgV225TBBc",
"vUV76d3Q_V0",
"Lk97xLk-7fg",
"RB5XL7_TPGg",
"P9Wf9d1f-II",
"Yqnzl5FcUN4",
"-JGdz3xbesA",
"fixEckTTyl0",
"jLaY1E-_Ng0",
"P6O4eQswLTE",
"RgJgiVE_Z7U",
"DNkUoW-B8IM",
"3UGie75y1GY",
"Jb6dn6AQ9YI",
"PhlONs16tUU",
"sW0giQOJ3BM",
"x537pshR2AE",
"Sw-eKD48ZVY",
"WFdWTCiAYrg",
"0-dlwdYJnXE",
"iTW3NS20ppY",
"qeBbsAqGlqc")

keyToVideo['stupid'] = ("qR-JyIXevXw",
"g3_ZvhXtOsM",
"HXG5-XTih0Y")

keyToVideo['surprised'] = ("HlEb6hNSaBg",
"S4hxiKIunCk",
"lF1eEmJBghI",
"H8ldJaNdq1c",
"asO6bL7oHxg",
"YGdlfGy7hJw",
"u6hooBrGEqc",
"0HRUycGW-bE",
"aFgIo2vT3EA",
"Bd904qxhhM4",
"CvZlf6uUuNQ",
"_5rWi_PwkI8",
"4ItC8QVuNs8",
"LryGHdOramk",
"UnzqSqAwONc",
"M5a85ArrNZw",
"sLtx_Fs6YOI",
"3r7Zja0Ira4",
"MMyxxRtHVTI",
"f4irEUeCNGg",
"sQRJI2pUKS8",
"ZjBigNTZIeM",
"QTaJ0ddSgsg",
"dmmjhbe8hII",
"4PJCGIYaYjQ",
"vKzbadHR6Ds",
"aiE9VqunjKA",
"KTKKovEb2hc",
"b8PNydXn2Pk",
"E9lkXwGEgj4",
"UKXqcKmlqB0",
"FgNI5TT7q98",
"4NuIHW-xiwA",
"1oDmnFZ8vYE",
"x0n7sKZE3lI",
"EUueVrRjxRQ",
"9mOVXtSjJaY",
"yuvzZA1EKSA",
"GXvYbLH1GBk",
"cjCedQR8M_s",
"OMs-vINwsc4",
"QuKYf6_gyvY",
"BoChmcVXtSw",
"tTcrZH2hBNw",
"o3rw8KhnhHI",
"EYpTzILQXGU",
"5yVKokkiskI",
"ax8zG3wapOs",
"HJ03Dory9vI")

keyToVideo['worried'] = ("Tk8h31sTxws",
"ON90FzdtPP0",
"TAnMl-tdoV4",
"M33zFPK39Uo",
"pLtzIMwiF2o",
"aUmlumZ9SiM",
"EmUt6x5vIrc",
"flzjEqwgkmk",
"c0wiZabrFos",
"Eg-2b5bJNuM",
"B-0T72ujt5o",
"aSCMBGzId2s",
"Z2X1gY_RZuk",
"-GQ_5SK4U3A",
"tAO2g40iRQ4",
"0tbHMNbh--w",
"tSDP5xlydzs",
"lA7tI9pVHsA",
"rnfllfOq2b4",
"urtl4ZGuJ9c",
"7ayY3VunNnc",
"jKGaG3rf6Ng",
"te9rw3KH788",
"s2Zf3vuo9fs",
"aLH_utR7vSE",
"GjNG2duNcXo",
"aSy9XLmcRo8",
"5km_gvJi_2I",
"tgviPl3a5Ds",
"xeuXmuT-Q2M",
"W5XN1DnK_b8",
"i0GSrpchz2Y",
"gp-UB5pTS_M",
"Q0avK4UEQqY",
"QrZ9fMGjxi0",
"5-MESEOgVhA",
"kwQuWwAarGk",
"k52nBJTOUPQ",
"Q5pWC8glqOw",
"E5KapRu7HVE",
"WtFwDMyTl_Y",
"66WnkGgOJSg",
"sft67DTC1s0",
"d8-MqSRgDSM",
"42gVneg6Ohw",
"aeJ2_zQ_a7Y",
"6V3rX1WGEFM",
"MhOB8h09v6w",
"zLmY-jQaNJI",
"OjXSE5PL3Dk",
"bjBqDBdLnVE",
"cJH-Tah878s",
"w5BqoYD4Z4I",
"7eLouhF93Oc",
"3XcCm8lvJ88",
"XLDW2WHMe7w",
"NdfmEjlj-Dg",
"sdTy9Iu3qD0",
"sYPAklSnToY",
"-2NOz-E5h_A",
"FqGBHS2BBXA",
"CHE1FDSfeS0",
"u6DKdI6EcX4",
"CxxtAI-7t4I",
"zKaOX20na8o",
"pP7x16LqoGE",
"EIycjItnA1M",
"xgSIaaw8ySc",
"3oNy3-Ffbgw",
"6hJkNqWKdsg",
"k-HnpeLdIsY",
"bMB-JjLic_A",
"tjnut3z-EAg",
"0FoFvxDj9Rk",
"bTW5JzxXaYs",
"QgNuVYrNs78",
"RgUzbro-CdY")
