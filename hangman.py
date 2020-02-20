import random
import os

words = ["able","about","account","acid","across","act","addition","adjustment","advertisement","after","again","against","agreement","air","all","almost","among","amount","amusement","and","angle","angry","animal","answer","ant","any","apparatus","apple","approval","arch","argument","arm","army","art","attack","attempt","attention","attraction","authority","automatic","awake","baby","back","bad","bag","balance","ball","band","base","basin","basket","bath","beautiful","because","bed","bee","before","behaviour","belief","bell","bent","berry","between","bird","birth","bit","bite","bitter","black","blade","blood","blow","blue","board","boat","body","boiling","bone","book","boot","bottle","box","boy","brain","brake","branch","brass","bread","breath","brick","bridge","bright","broken","brother","brown","brush","bucket","building","bulb","burn","burst","business","but","butter","button","by","cake","camera","canvas","card","care","carriage","cart","cat","cause","certain","chain","chalk","chance","change","cheap","cheese","chemical","chest","chief","chin","church","circle","clean","clear","clock","cloth","cloud","coal","coat","cold","collar","colour","comb","come","comfort","committee","common","company","comparison","competition","complete","complex","condition","connection","conscious","control","cook","copper","copy","cord","cork","cotton","cough","country","cover","cow","crack","credit","crime","cruel","crush","cry","cup","cup","current","curtain","curve","cushion","damage","danger","dark","daughter","day","dead","dear","death","debt","decision","deep","degree","delicate","dependent","design","desire","destruction","detail","development","different","digestion","direction","dirty","discovery","discussion","disease","disgust","distance","distribution","division","do","dog","door","doubt","down","drain","drawer","dress","drink","driving","drop","dry","dust","ear","early","earth","east","edge","education","effect","egg","elastic","electric","end","engine","enough","equal","error","even","event","ever","every","example","exchange","existence","expansion","experience","expert","eye","face","fact","fall","false","family","far","farm","fat","father","fear","feather","feeble","feeling","female","fertile","fiction","field","fight","finger","fire","first","fish","fixed","flag","flame","flat","flight","floor","flower","fly","fold","food","foolish","foot","for","force","fork","form","forward","fowl","frame","free","frequent","friend","from","front","fruit","full","future","garden","general","get","girl","give","glass","glove","go","goat","gold","good","government","grain","grass","great","green","grey","grip","group","growth","guide","gun","hair","hammer","hand","hanging","happy","harbour","hard","harmony","hat","hate","have","he","head","healthy","hear","hearing","heart","heat","help","high","history","hole","hollow","hook","hope","horn","horse","hospital","hour","house","how","humour","I","ice","idea","if","ill","important","impulse","in","increase","industry","ink","insect","instrument","insurance","interest","invention","iron","island","jelly","jewel","join","journey","judge","jump","keep","kettle","key","kick","kind","kiss","knee","knife","knot","knowledge","land","language","last","late","laugh","law","lead","leaf","learning","leather","left","leg","let","letter","level","library","lift","light","like","limit","line","linen","lip","liquid","list","little","living","lock","long","look","loose","loss","loud","love","low","machine","make","male","man","manager","map","mark","market","married","mass","match","material","may","meal","measure","meat","medical","meeting","memory","metal","middle","military","milk","mind","mine","minute","mist","mixed","money","monkey","month","moon","morning","mother","motion","mountain","mouth","move","much","muscle","music","nail","name","narrow","nation","natural","near","necessary","neck","need","needle","nerve","net","new","news","night","no","noise","normal","north","nose","not","note","now","number","nut","observation","of","off","offer","office","oil","old","on","only","open","operation","opinion","opposite","or","orange","order","organization","ornament","other","out","oven","over","owner","page","pain","paint","paper","parallel","parcel","part","past","paste","payment","peace","pen","pencil","person","physical","picture","pig","pin","pipe","place","plane","plant","plate","play","please","pleasure","plough","pocket","point","poison","polish","political","poor","porter","position","possible","pot","potato","powder","power","present","price","print","prison","private","probable","process","produce","profit","property","prose","protest","public","pull","pump","punishment","purpose","push","put","quality","question","quick","quiet","quite","rail","rain","range","rat","rate","ray","reaction","reading","ready","reason","receipt","record","red","regret","regular","relation","religion","representative","request","respect","responsible","rest","reward","rhythm","rice","right","ring","river","road","rod","roll","roof","room","root","rough","round","rub","rule","run","sad","safe","sail","salt","same","sand","say","scale","school","science","scissors","screw","sea","seat","second","secret","secretary","see","seed","seem","selection","self","send","sense","separate","serious","servant","sex","shade","shake","shame","sharp","sheep","shelf","ship","shirt","shock","shoe","short","shut","side","sign","silk","silver","simple","sister","size","skin","","skirt","sky","sleep","slip","slope","slow","small","smash","smell","smile","smoke","smooth","snake","sneeze","snow","so","soap","society","sock","soft","solid","some","","son","song","sort","sound","soup","south","space","spade","special","sponge","spoon","spring","square","stage","stamp","star","start","statement","station","steam","steel","stem","step","stick","sticky","stiff","still","stitch","stocking","stomach","stone","stop","store","story","straight","strange","street","stretch","strong","structure","substance","such","sudden","sugar","suggestion","summer","sun","support","surprise","sweet","swim","system","table","tail","take","talk","tall","taste","tax","teaching","tendency","test","than","that","the","then","theory","there","thick","thin","thing","this","thought","thread","throat","through","through","thumb","thunder","ticket","tight","till","time","tin","tired","to","toe","together","tomorrow","tongue","tooth","top","touch","town","trade","train","transport","tray","tree","trick","trouble","trousers","true","turn","twist","umbrella","under","unit","up","use","value","verse","very","vessel","view","violent","voice","waiting","walk","wall","war","warm","wash","waste","watch","water","wave","wax","way","weather","week","weight","well","west","wet","wheel","when","where","while","whip","whistle","white","who","why","wide","will","wind","window","wine","wing","winter","wire","wise","with","woman","wood","wool","word","work","worm","wound","writing","wrong","year","yellow","yes","yesterday","you","young"]

random_word = words[random.randint(0, len(words))]


def image(strikes):             # draws the hangmans noose as a function of how many strikes you have

    noose1 = "   ____  "
    noose2 = "  |    | "
    noose3 = "  |      "
    noose4 = "  |      "
    noose5 = "  |      "
    noose6 = " _|_     "
    noose7 = "|   |___ "
    noose8 = "|_ _ _ _|"
    if strikes == 0:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |      "
        noose4 = "  |      "
        noose5 = "  |      "
        noose6 = " _|_     "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes == 1:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |    O "
        noose4 = "  |      "
        noose5 = "  |      "
        noose6 = " _|_     "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes == 2:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |    O "
        noose4 = "  |    | "
        noose5 = "  |      "
        noose6 = " _|_     "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes == 3:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |    O "
        noose4 = "  |   /| "
        noose5 = "  |      "
        noose6 = " _|_     "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes == 4:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |    O "
        noose4 = "  |   /|\ "
        noose5 = "  |      "
        noose6 = " _|_     "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes == 5:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |    O "
        noose4 = "  |   /|\ "
        noose5 = "  |    | "
        noose6 = " _|_     "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes == 6:
        noose1 = "   ____  "
        noose2 = "  |    | "
        noose3 = "  |    O "
        noose4 = "  |   /|\ "
        noose5 = "  |    | "
        noose6 = " _|_  /  "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    if strikes >= 7:
        noose1 = "   ____  "
        noose2 = "  |    | *dead*"
        noose3 = "  |    O "
        noose4 = "  |   /|\ "
        noose5 = "  |    | "
        noose6 = " _|_  / \ "
        noose7 = "|   |___ "
        noose8 = "|_ _ _ _|"
    return str(noose1 + "\n" + noose2 + "\n" + noose3 + "\n" + noose4 + "\n" + noose5 + "\n" + noose6 + "\n" + noose7 + "\n" + noose8 + "\n")


def hangman(word):                           # plays hangman as a function of a random word from the list

    w_o_r_d = list(word)                     # splits random word into individual letters
    blanks = "_" * len(word)                 # creates "_ _ _ _ _" to show how many letters the word has to guess
    b_l_a_n_k_s = list(blanks)               # splits each "_" into its own letter for replacement
    max_guesses = len(word) + 7              # sets the maximum guesses as a function of the length of the word
    strikes = 0                              # sets strikes to zero
    incorrect = ""                           # creates initial string of incorrect guesses
    guesses_left = max_guesses               # how many guesses player gets
    guessed = ""                             # initial string of all guesses
    # print("\nWord (for testing): " + word)    # remove comment to see word printed

    while 7 - strikes > 0:                   # as long as player hasn't struck out hangman continues to play

        os.system("cls")                     # clears screen after every guess for reprinting

        if "".join(b_l_a_n_k_s) == "".join(w_o_r_d):    # if the player has guessed the word the while loop breaks
            break

        print(image(strikes))                               # prints noose as a function of how many strikes
        print("Strikes remaining: " + str(7 - strikes))     # tells the student how many strikes they have left
        print("You\'ve guessed: " + incorrect)              # tells player what their incorrect guesses are
        print("Word: "+" ".join(b_l_a_n_k_s))               # tells player the blanks of the word + whatever correct guesses they have
        guess = input("\nGuess a letter or word: ")         # tells player to guess a letter or word
        g_u_e_s_s = list(guess)                             # splits letters of guess into a list

        for letter in g_u_e_s_s:                            # for each letter in players guess
            location = 0
            if letter not in guessed:                       # if the letter hasnt been guessed adds the letter to "guessed" and takes away a guess
                guessed += letter
                guesses_left -= 1

                if letter not in w_o_r_d:                   # if the letter isn't in the word and and hasn't been guessed
                    if letter not in incorrect:             # adds letter to incorrect string and adds a strike
                        incorrect += letter
                        strikes += 1
                    else:                                   # if letter is in incorrect already guesses +1
                        guesses_left += 1
                else:
                    for letters in w_o_r_d:                 # if letter is in word, checks each letter in guess against
                        if letters == letter:               # each letter in the word and substitutes letter in for "_"
                            b_l_a_n_k_s[location] = letter  # in correct location if correct
                        location += 1

        if strikes >= 7:                                    # if strikes is more than 7 while loop breaks
            break                                           # and prints a dead guy + message telling what word is.
    if strikes >= 7:
        image(strikes)
        print("Silly! The word was: " + word)               # if player guessed word, congratulates.
    else:
        print("   " + " ".join(b_l_a_n_k_s))
        print("You guessed it! The word was: " + word)
    if input("Play again? y/n\n") == "y":
        print("Yay hangman! All words are made up of letters only, no -\'s or spaces will be present.\n")
        hangman(words[random.randint(0, len(words))])


print("Yay hangman! All words are made up of letters only, no -\'s or spaces will be present.\n")
hangman(words[random.randint(0, len(words))])
