# Converted to a python Slack bot by Mensly
#
# Original source by Joe Sabia and Aaron Rasmussen
# http://theofficestaremachine.com/
import random
import json
from flask import Flask, Response, request
app = Flask(__name__)

emotion_to_key = {}
key_to_video = {}

emotion_to_key["1999"] = "1999"
emotion_to_key["amused"] = "amused"
emotion_to_key["charmed"] = "amused"
emotion_to_key["cheery"] = "amused"
emotion_to_key["diverted"] = "amused"
emotion_to_key["employed"] = "amused"
emotion_to_key["engaged"] = "amused"
emotion_to_key["engrossed"] = "amused"
emotion_to_key["entertained"] = "amused"
emotion_to_key["tickled"] = "amused"
emotion_to_key["amusing"] = "amused"
emotion_to_key["diverted"] = "amused"
emotion_to_key["cheery"] = "amused"
emotion_to_key["engaged"] = "amused"
emotion_to_key["employed"] = "amused"
emotion_to_key["entertained"] = "amused"
emotion_to_key["engrossed"] = "amused"
emotion_to_key["entertained"] = "amused"
emotion_to_key["cheery"] = "amused"
emotion_to_key["diverted"] = "amused"
emotion_to_key["employed"] = "amused"
emotion_to_key["laughing"] = "amused"
emotion_to_key["laughter"] = "amused"
emotion_to_key["shame"] = "embarrassed"
emotion_to_key["shameful"] = "embarrassed"
emotion_to_key["awkward"] = "embarrassed"
emotion_to_key["uncomfortable"] = "embarrassed"
emotion_to_key["grumpy"] = "angry"
emotion_to_key["acrimonious"] = "angry"
emotion_to_key["apoplectic"] = "angry"
emotion_to_key["infuriated"] = "angry"
emotion_to_key["frustrated"] = "angry"
emotion_to_key["frustration"] = "angry"
emotion_to_key["bad-tempered"] = "angry"
emotion_to_key["bitter"] = "angry"
emotion_to_key["choleric"] = "angry"
emotion_to_key["cross"] = "angry"
emotion_to_key["enraged"] = "angry"
emotion_to_key["fuming"] = "angry"
emotion_to_key["furious"] = "angry"
emotion_to_key["heated"] = "angry"
emotion_to_key["ill-natured"] = "angry"
emotion_to_key["ill-tempered"] = "angry"
emotion_to_key["incensed"] = "angry"
emotion_to_key["indignant"] = "angry"
emotion_to_key["infurious"] = "angry"
emotion_to_key["irate"] = "angry"
emotion_to_key["livid"] = "angry"
emotion_to_key["mad"] = "angry"
emotion_to_key["outraged"] = "angry"
emotion_to_key["passionate"] = "angry"
emotion_to_key["pissed"] = "angry"
emotion_to_key["aggressive"] = "angry"
emotion_to_key["raging"] = "angry"
emotion_to_key["seething"] = "angry"
emotion_to_key["sore"] = "angry"
emotion_to_key["steamed"] = "angry"
emotion_to_key["stormy"] = "angry"
emotion_to_key["vexed"] = "angry"
emotion_to_key["wrathful"] = "angry"
emotion_to_key["angry"] = "angry"
emotion_to_key["mean"] = "angry"
emotion_to_key["deadly"] = "angry"
emotion_to_key["scary"] = "angry"
emotion_to_key["murderous"] = "angry"
emotion_to_key["anger"] = "angry"
emotion_to_key["homicidal"] = "crazy"
emotion_to_key["intense"] = "crazy"
emotion_to_key["cranky"] = "annoyed"
emotion_to_key["sassy"] = "annoyed"
emotion_to_key["aggravated"] = "annoyed"
emotion_to_key["antagonized"] = "annoyed"
emotion_to_key["attacked"] = "annoyed"
emotion_to_key["bugged"] = "annoyed"
emotion_to_key["chagrined"] = "annoyed"
emotion_to_key["disgruntled"] = "annoyed"
emotion_to_key["displeased"] = "annoyed"
emotion_to_key["exasperated"] = "annoyed"
emotion_to_key["frosty"] = "annoyed"
emotion_to_key["galled"] = "annoyed"
emotion_to_key["irked"] = "annoyed"
emotion_to_key["irritated"] = "annoyed"
emotion_to_key["miffed"] = "annoyed"
emotion_to_key["nerved"] = "annoyed"
emotion_to_key["gruntled"] = "gruntled"
emotion_to_key["nettled"] = "annoyed"
emotion_to_key["peeved"] = "annoyed"
emotion_to_key["piqued"] = "annoyed"
emotion_to_key["sarcastic"] = "annoyed"
emotion_to_key["riled"] = "annoyed"
emotion_to_key["sore"] = "annoyed"
emotion_to_key["ticked"] = "annoyed"
emotion_to_key["unnerved"] = "annoyed"
emotion_to_key["annoyed"] = "annoyed"
emotion_to_key["disinterested"] = "bored"
emotion_to_key["dull"] = "bored"
emotion_to_key["stultified"] = "bored"
emotion_to_key["stupefied"] = "bored"
emotion_to_key["tedious"] = "bored"
emotion_to_key["uninterested"] = "bored"
emotion_to_key["bored"] = "bored"
emotion_to_key["ambivalent"] = "bored"
emotion_to_key["ennui"] = "bored"
emotion_to_key["confident"] = "confident"
emotion_to_key["arrogant"] = "confident"
emotion_to_key["assertive"] = "confident"
emotion_to_key["assured"] = "confident"
emotion_to_key["certain"] = "confident"
emotion_to_key["committed"] = "confident"
emotion_to_key["convinced"] = "confident"
emotion_to_key["coolheaded"] = "confident"
emotion_to_key["determined"] = "confident"
emotion_to_key["hopeful"] = "confident"
emotion_to_key["imperturbable"] = "confident"
emotion_to_key["levelheaded"] = "confident"
emotion_to_key["optimistic"] = "confident"
emotion_to_key["persuaded"] = "confident"
emotion_to_key["poised"] = "confident"
emotion_to_key["positive"] = "confident"
emotion_to_key["positive"] = "confident"
emotion_to_key["resolute"] = "confident"
emotion_to_key["sanguine"] = "confident"
emotion_to_key["satisfied"] = "confident"
emotion_to_key["self-assured"] = "confident"
emotion_to_key["self-confident"] = "confident"
emotion_to_key["self-possessed"] = "confident"
emotion_to_key["self-reliant"] = "confident"
emotion_to_key["unperturbed"] = "confident"
emotion_to_key["unruffled"] = "confident"
emotion_to_key["addled"] = "confused"
emotion_to_key["befuddled"] = "confused"
emotion_to_key["bewildered"] = "confused"
emotion_to_key["bemused"] = "confused"
emotion_to_key["blurred"] = "confused"
emotion_to_key["confounded"] = "confused"
emotion_to_key["demented"] = "confused"
emotion_to_key["dim"] = "confused"
emotion_to_key["disorientated"] = "confused"
emotion_to_key["disoriented"] = "confused"
emotion_to_key["hazy"] = "confused"
emotion_to_key["imprecise"] = "confused"
emotion_to_key["indistinct"] = "confused"
emotion_to_key["muddled"] = "confused"
emotion_to_key["mystified"] = "confused"
emotion_to_key["nonplussed"] = "confused"
emotion_to_key["senile"] = "confused"
emotion_to_key["shadowy"] = "confused"
emotion_to_key["sketchy"] = "confused"
emotion_to_key["unbalanced"] = "confused"
emotion_to_key["unclear"] = "confused"
emotion_to_key["unhinged"] = "confused"
emotion_to_key["vague"] = "confused"
emotion_to_key["woolly"] = "confused"
emotion_to_key["confused"] = "confused"
emotion_to_key["perplexed"] = "confused"
emotion_to_key["perplexing"] = "confused"
emotion_to_key["crazy"] = "crazy"
emotion_to_key["insane"] = "crazy"
emotion_to_key["dangerous"] = "crazy"
emotion_to_key["creepy"] = "creepy"
emotion_to_key["weird"] = "creepy"
emotion_to_key["acquiescent"] = "defeated"
emotion_to_key["compliant"] = "defeated"
emotion_to_key["regretful"] = "defeated"
emotion_to_key["regret"] = "defeated"
emotion_to_key["dismissed"] = "defeated"
emotion_to_key["fatalistic"] = "defeated"
emotion_to_key["forbearing"] = "defeated"
emotion_to_key["passive"] = "defeated"
emotion_to_key["patient"] = "defeated"
emotion_to_key["philosophical"] = "defeated"
emotion_to_key["rejected"] = "defeated"
emotion_to_key["resigned"] = "defeated"
emotion_to_key["stoical"] = "defeated"
emotion_to_key["submissive"] = "defeated"
emotion_to_key["uncomplaining"] = "defeated"
emotion_to_key["defeated"] = "defeated"
emotion_to_key["drunk"] = "drunk"
emotion_to_key["evil"] = "evil"
emotion_to_key["demonic"] = "evil"
emotion_to_key["satanic"] = "evil"
emotion_to_key["devilish"] = "evil"
emotion_to_key["diabolical"] = "evil"
emotion_to_key["underhanded"] = "devious"
emotion_to_key["deceitful"] = "devious"
emotion_to_key["dishonest"] = "devious"
emotion_to_key["dishonorable"] = "devious"
emotion_to_key["unethical"] = "devious"
emotion_to_key["unprincipled"] = "devious"
emotion_to_key["immoral"] = "devious"
emotion_to_key["unscrupulous"] = "devious"
emotion_to_key["fraudulent"] = "devious"
emotion_to_key["dubious"] = "devious"
emotion_to_key["unfair"] = "devious"
emotion_to_key["treacherous"] = "devious"
emotion_to_key["duplicitous"] = "devious"
emotion_to_key["crafty"] = "devious"
emotion_to_key["cunning"] = "devious"
emotion_to_key["calculating"] = "devious"
emotion_to_key["artful"] = "devious"
emotion_to_key["conniving"] = "devious"
emotion_to_key["scheming"] = "devious"
emotion_to_key["sly"] = "devious"
emotion_to_key["wily"] = "devious"
emotion_to_key["sneaky"] = "devious"
emotion_to_key["furtive"] = "devious"
emotion_to_key["secretive"] = "devious"
emotion_to_key["clandestine"] = "devious"
emotion_to_key["surreptitious"] = "devious"
emotion_to_key["covert"] = "devious"
emotion_to_key["snide"] = "devious"
emotion_to_key["crooked"] = "devious"
emotion_to_key["shady"] = "devious"
emotion_to_key["dirty"] = "devious"
emotion_to_key["devious"] = "devious"
emotion_to_key["icy"] = "devious"
emotion_to_key["appalled"] = "disgusted"
emotion_to_key["horrified"] = "disgusted"
emotion_to_key["nauseating"] = "disgusted"
emotion_to_key["offensive"] = "disgusted"
emotion_to_key["offended"] = "disgusted"
emotion_to_key["repellent"] = "disgusted"
emotion_to_key["repulsive"] = "disgusted"
emotion_to_key["scandalized"] = "disgusted"
emotion_to_key["shocking"] = "disgusted"
emotion_to_key["sick"] = "disgusted"
emotion_to_key["sickening"] = "disgusted"
emotion_to_key["contempt"] = "disgusted"
emotion_to_key["disgusted"] = "disgusted"
emotion_to_key["abashed"] = "embarrassed"
emotion_to_key["ashamed"] = "embarrassed"
emotion_to_key["discomposed"] = "embarrassed"
emotion_to_key["bashful"] = "embarrassed"
emotion_to_key["blushing"] = "embarrassed"
emotion_to_key["chagrined"] = "embarrassed"
emotion_to_key["discomfited"] = "embarrassed"
emotion_to_key["discomposed"] = "embarrassed"
emotion_to_key["disconcerted"] = "embarrassed"
emotion_to_key["flustered"] = "embarrassed"
emotion_to_key["humiliated"] = "embarrassed"
emotion_to_key["mortified"] = "embarrassed"
emotion_to_key["self-conscious"] = "embarrassed"
emotion_to_key["shamed"] = "embarrassed"
emotion_to_key["shamefaced"] = "embarrassed"
emotion_to_key["sheepish"] = "embarrassed"
emotion_to_key["shy"] = "embarrassed"
emotion_to_key["shy"] = "embarrassed"
emotion_to_key["tongue-tied"] = "embarrassed"
emotion_to_key["embarrassed"] = "embarrassed"
emotion_to_key["sensitive"] = "embarrassed"
emotion_to_key["embarassed"] = "embarrassed"
emotion_to_key["funny"] = "funny"
emotion_to_key["silly"] = "funny"
emotion_to_key["hilarious"] = "funny"
emotion_to_key["goofy"] = "funny"
emotion_to_key["ridiculous"] = "funny"
emotion_to_key["guilty"] = "guilty"
emotion_to_key["excited"] = "crazy"
emotion_to_key["stoked"] = "crazy"
emotion_to_key["excitable"] = "crazy"
emotion_to_key["extreme"] = "crazy"
emotion_to_key["ebullient"] = "happy"
emotion_to_key["beaming"] = "happy"
emotion_to_key["beatific"] = "happy"
emotion_to_key["blissful"] = "happy"
emotion_to_key["blithe"] = "happy"
emotion_to_key["buoyant"] = "happy"
emotion_to_key["carefree"] = "happy"
emotion_to_key["cheerful"] = "happy"
emotion_to_key["cheery"] = "happy"
emotion_to_key["chirpy"] = "happy"
emotion_to_key["contented"] = "happy"
emotion_to_key["love"] = "happy"
emotion_to_key["loving"] = "happy"
emotion_to_key["delighted"] = "happy"
emotion_to_key["ecstatic"] = "happy"
emotion_to_key["elated"] = "happy"
emotion_to_key["euphoric"] = "happy"
emotion_to_key["exhilarated"] = "happy"
emotion_to_key["exultant"] = "happy"
emotion_to_key["gleeful"] = "happy"
emotion_to_key["gratified"] = "happy"
emotion_to_key["grinning"] = "happy"
emotion_to_key["jocular"] = "happy"
emotion_to_key["jocund"] = "happy"
emotion_to_key["jolly"] = "happy"
emotion_to_key["jovial"] = "happy"
emotion_to_key["joyful"] = "happy"
emotion_to_key["joyous"] = "happy"
emotion_to_key["jubilant"] = "happy"
emotion_to_key["lighthearted"] = "happy"
emotion_to_key["merry"] = "happy"
emotion_to_key["overjoyed"] = "happy"
emotion_to_key["radiant"] = "happy"
emotion_to_key["rapturous"] = "happy"
emotion_to_key["satisfied"] = "happy"
emotion_to_key["smiling"] = "happy"
emotion_to_key["sunny"] = "happy"
emotion_to_key["thrilled"] = "happy"
emotion_to_key["untroubled"] = "happy"
emotion_to_key["happy"] = "happy"
emotion_to_key["horny"] = "horny"
emotion_to_key["seductive"] = "horny"
emotion_to_key["aroused"] = "horny"
emotion_to_key["sexy"] = "horny"
emotion_to_key["flirty"] = "horny"
emotion_to_key["sexual"] = "horny"
emotion_to_key["sultry"] = "horny"
emotion_to_key["lovey"] = "horny"
emotion_to_key["romantic"] = "horny"
emotion_to_key["starving"] = "hungry"
emotion_to_key["hangry"] = "hungry"
emotion_to_key["hungry"] = "hungry"
emotion_to_key["absorbing"] = "intrigued"
emotion_to_key["appealing"] = "intrigued"
emotion_to_key["arousing"] = "intrigued"
emotion_to_key["captivated"] = "intrigued"
emotion_to_key["compelling"] = "intrigued"
emotion_to_key["curious"] = "intrigued"
emotion_to_key["enchanted"] = "intrigued"
emotion_to_key["engaged"] = "intrigued"
emotion_to_key["enthralled"] = "intrigued"
emotion_to_key["fascinated"] = "intrigued"
emotion_to_key["gripping"] = "intrigued"
emotion_to_key["interested"] = "intrigued"
emotion_to_key["piquing"] = "intrigued"
emotion_to_key["riveting"] = "intrigued"
emotion_to_key["intrigued"] = "intrigued"
emotion_to_key["jealous"] = "jealous"
emotion_to_key["envious"] = "jealous"
emotion_to_key["smug"] = "proud"
emotion_to_key["content"] = "proud"
emotion_to_key["contented"] = "proud"
emotion_to_key["glad"] = "proud"
emotion_to_key["satisfied"] = "proud"
emotion_to_key["thankful"] = "proud"
emotion_to_key["pleased"] = "proud"
emotion_to_key["sardonic"] = "proud"
emotion_to_key["complacent"] = "proud"
emotion_to_key["proud"] = "proud"
emotion_to_key["grateful"] = "relieved"
emotion_to_key["reassured"] = "relieved"
emotion_to_key["reassuring"] = "relieved"
emotion_to_key["thankful"] = "relieved"
emotion_to_key["relieved"] = "relieved"
emotion_to_key["lonely"] = "sad"
emotion_to_key["hurt"] = "sad"
emotion_to_key["disappointed"] = "sad"
emotion_to_key["sentimental"] = "sad"
emotion_to_key["sappy"] = "sad"
emotion_to_key["bummed"] = "sad"
emotion_to_key["awful"] = "sad"
emotion_to_key["blah"] = "sad"
emotion_to_key["blue"] = "sad"
emotion_to_key["crestfallen"] = "sad"
emotion_to_key["dejected"] = "sad"
emotion_to_key["depressed"] = "sad"
emotion_to_key["desolate"] = "sad"
emotion_to_key["despairing"] = "sad"
emotion_to_key["despondent"] = "sad"
emotion_to_key["disconsolate"] = "sad"
emotion_to_key["dismal"] = "sad"
emotion_to_key["doleful"] = "sad"
emotion_to_key["down"] = "sad"
emotion_to_key["downcast"] = "sad"
emotion_to_key["forlorn"] = "sad"
emotion_to_key["gloomy"] = "sad"
emotion_to_key["glum"] = "sad"
emotion_to_key["harrowing"] = "sad"
emotion_to_key["heartbreaking"] = "sad"
emotion_to_key["heartbroken"] = "sad"
emotion_to_key["heartrending"] = "sad"
emotion_to_key["inconsolable"] = "sad"
emotion_to_key["melancholy"] = "sad"
emotion_to_key["miserable"] = "sad"
emotion_to_key["miserable"] = "sad"
emotion_to_key["mournful"] = "sad"
emotion_to_key["pathetic"] = "sad"
emotion_to_key["pitiful"] = "sad"
emotion_to_key["sorrowful"] = "sad"
emotion_to_key["sorry"] = "sad"
emotion_to_key["tragic"] = "sad"
emotion_to_key["traumatic"] = "sad"
emotion_to_key["unfortunate"] = "sad"
emotion_to_key["unhappy"] = "sad"
emotion_to_key["unhappy"] = "sad"
emotion_to_key["woebegone"] = "sad"
emotion_to_key["wretched"] = "sad"
emotion_to_key["sad"] = "sad"
emotion_to_key["deep"] = "deadpan"
emotion_to_key["contemplative"] = "serious"
emotion_to_key["deep"] = "serious"
emotion_to_key["apathetic"] = "serious"
emotion_to_key["callous"] = "serious"
emotion_to_key["cold"] = "serious"
emotion_to_key["cool"] = "serious"
emotion_to_key["dour"] = "serious"
emotion_to_key["earnest"] = "serious"
emotion_to_key["earnest"] = "serious"
emotion_to_key["emotionless"] = "serious"
emotion_to_key["frigid"] = "serious"
emotion_to_key["genuine"] = "serious"
emotion_to_key["constipated"] = "serious"
emotion_to_key["grave"] = "serious"
emotion_to_key["grim"] = "serious"
emotion_to_key["humorless"] = "serious"
emotion_to_key["impassive"] = "serious"
emotion_to_key["passionless"] = "serious"
emotion_to_key["pensive"] = "pensive"
emotion_to_key["quixotic"] = "pensive"
emotion_to_key["perfunctory"] = "serious"
emotion_to_key["phlegmatic"] = "serious"
emotion_to_key["poker-faced"] = "serious"
emotion_to_key["reserved"] = "serious"
emotion_to_key["restrained"] = "serious"
emotion_to_key["sincere"] = "serious"
emotion_to_key["sober"] = "serious"
emotion_to_key["solemn"] = "serious"
emotion_to_key["somber"] = "serious"
emotion_to_key["stern"] = "serious"
emotion_to_key["stoic"] = "serious"
emotion_to_key["stoical"] = "serious"
emotion_to_key["stony-faced"] = "serious"
emotion_to_key["thoughtful"] = "pensive"
emotion_to_key["undemonstrative"] = "serious"
emotion_to_key["unemotional"] = "serious"
emotion_to_key["unexcitable"] = "serious"
emotion_to_key["unfeeling"] = "serious"
emotion_to_key["unsentimental"] = "serious"
emotion_to_key["unsmiling"] = "serious"
emotion_to_key["wholehearted"] = "serious"
emotion_to_key["serious"] = "serious"
emotion_to_key["amazed"] = "serious"
emotion_to_key["blank"] = "serious"
emotion_to_key["indifferent"] = "serious"
emotion_to_key["stupid"] = "stupid"
emotion_to_key["dumb"] = "stupid"
emotion_to_key["suprised"] = "surprised"
emotion_to_key["astonished"] = "surprised"
emotion_to_key["astounded"] = "surprised"
emotion_to_key["incredulous"] = "surprised"
emotion_to_key["flabbergasted"] = "surprised"
emotion_to_key["dazed"] = "surprised"
emotion_to_key["dumbfounded"] = "surprised"
emotion_to_key["dumbstruck"] = "surprised"
emotion_to_key["floored"] = "surprised"
emotion_to_key["flummoxed"] = "surprised"
emotion_to_key["shaken"] = "surprised"
emotion_to_key["shocked"] = "surprised"
emotion_to_key["disbelieving"] = "surprised"
emotion_to_key["speechless"] = "surprised"
emotion_to_key["staggered"] = "surprised"
emotion_to_key["startled"] = "surprised"
emotion_to_key["stunned"] = "surprised"
emotion_to_key["stupefied"] = "surprised"
emotion_to_key["thunderstruck"] = "surprised"
emotion_to_key["surprised"] = "surprised"
emotion_to_key["lethargic"] = "confused"
emotion_to_key["tired"] = "sad"
emotion_to_key["lazy"] = "sad"
emotion_to_key["jaded"] = "sad"
emotion_to_key["bushed"] = "sad"
emotion_to_key["dead"] = "sad"
emotion_to_key["jaded"] = "sad"
emotion_to_key["dog-tired"] = "sad"
emotion_to_key["drained"] = "sad"
emotion_to_key["enervated"] = "sad"
emotion_to_key["exhausted"] = "sad"
emotion_to_key["fatigued"] = "sad"
emotion_to_key["jaded"] = "sad"
emotion_to_key["sleepy"] = "sad"
emotion_to_key["knackered"] = "sad"
emotion_to_key["pooped"] = "sad"
emotion_to_key["wasted"] = "sad"
emotion_to_key["weary"] = "sad"
emotion_to_key["zonked"] = "sad"
emotion_to_key["crying"] = "sad"
emotion_to_key["agitated"] = "worried"
emotion_to_key["agonized"] = "worried"
emotion_to_key["fearful"] = "worried"
emotion_to_key["anxious"] = "worried"
emotion_to_key["fear"] = "worried"
emotion_to_key["bedeviled"] = "worried"
emotion_to_key["bothered"] = "worried"
emotion_to_key["brooding"] = "worried"
emotion_to_key["concerned"] = "worried"
emotion_to_key["disquieted"] = "worried"
emotion_to_key["distressed"] = "worried"
emotion_to_key["disturbed"] = "worried"
emotion_to_key["flustered"] = "worried"
emotion_to_key["fretted"] = "worried"
emotion_to_key["nervous"] = "worried"
emotion_to_key["panicked"] = "worried"
emotion_to_key["perturbed"] = "worried"
emotion_to_key["plagued"] = "worried"
emotion_to_key["preoccupied"] = "worried"
emotion_to_key["rattled"] = "worried"
emotion_to_key["scared"] = "worried"
emotion_to_key["terrified"] = "worried"
emotion_to_key["afraid"] = "worried"
emotion_to_key["stewed"] = "worried"
emotion_to_key["stressed"] = "worried"
emotion_to_key["taxing"] = "worried"
emotion_to_key["tormented"] = "worried"
emotion_to_key["tormented"] = "worried"
emotion_to_key["troubled"] = "worried"
emotion_to_key["unsettled"] = "worried"
emotion_to_key["upset"] = "worried"
emotion_to_key["worried"] = "worried"


key_to_video['1999'] =  ("TA8oR4PUdZU",
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

key_to_video['amused'] =  ("thx77DeHLZY",
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

key_to_video['angry'] =  ("93F60yL5kMw",
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

key_to_video['annoyed'] = ("xp12AxZstak",
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

key_to_video['bored'] = ("KO45TUVjayA",
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

key_to_video['gruntled'] = ("2joetGgluqc",
"2joetGgluqc")

key_to_video['confident'] = ("zi_L9LE3l-U",
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

key_to_video['confused'] = ("vmnoUN2_3w8",
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

key_to_video['crazy'] = ("Z_TSkPivPpg",
"NuHVr6GLhWo",
"_dw4kgWLV1I",
"3rvxCiazeHw")

key_to_video['creepy'] = ("5mMRrkMmXjI",
"wSslbmoRpK4",
"h1ZEgnuGH2Q",
"5Ae8-Ehm1pU",
"kk1LcL7dZTc")

key_to_video['defeated'] = ("0roSsayezn4",
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

key_to_video['devious'] = (
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

key_to_video['disgusted'] = ("BV4h9JPbG2o",
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

key_to_video['drunk'] = ("I2EM9aucz6s",
"oWgDT9J-k5c",
"4XR-3kwaNKg")

key_to_video['embarrassed'] = ("rPvBS1wR89I",
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

key_to_video['evil'] = ("rPTABGn52-Q",
"rPTABGn52-Q",
"kYy36UbZ92o")

key_to_video['funny'] = ("TJxwipvr9mc",
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

key_to_video['guilty'] = ("U2TvBfzEhVo",
"nJk8RcWG5_M")

key_to_video['happy'] = ("w0XZDn94-Js",
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

key_to_video['horny'] = ("LbKdoJqJWy8",
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

key_to_video['hungry'] = ("L08kScTCJ8E",
"emZG_EchST4",
"GRKPlbJXL7c",
"5qNdPYpdeis",
"UgtjZOuiP6g")

key_to_video['intrigued'] = ("wRmIxCBJHyo",
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

key_to_video['jealous'] = ("5XrQkhFHBfE",
"SkvxeTVAOO0",
"zIutEXJ5j_g")




key_to_video['pensive'] = ("mEGHM4UdBqM",
"usD2gZYuDc0")

key_to_video['proud'] = ("ZEOThui7lRE",
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

key_to_video['relieved'] = ("wnLuUsFPCP4",
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

key_to_video['sad'] = ("eQSUrp-Ybu8",
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

key_to_video['serious'] =  ("wbobYVA2NEE",
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

key_to_video['stupid'] = ("qR-JyIXevXw",
"g3_ZvhXtOsM",
"HXG5-XTih0Y")

key_to_video['surprised'] = ("HlEb6hNSaBg",
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

key_to_video['worried'] = ("Tk8h31sTxws",
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

def get_video_url(emotion):
    try:
        video_id = random.choice(key_to_video[emotion_to_key[emotion]])
    except KeyError:
        video_id = "H07zYvkNYL8"
    return "https://youtu.be/" + video_id

@app.route('/', methods=['POST'])
def office_stare():
    emotion = request.form['text']
    url = get_video_url(emotion)
    response = dict(text=url, response_type="in_channel")
    return Response(json.dumps(response), mimetype='application/json')

if __name__ == "__main__":
    app.run()
