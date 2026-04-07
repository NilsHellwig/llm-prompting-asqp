import re, string


def exchange_phrases(asp_current, asp_exchange, text, returnFalseError = False):
    # create dict with phrases and their exchange
    phrases_dict = {}
    for idx, asp in enumerate(asp_current):
        if asp[0] != "NULL":
            phrases_dict[asp[0]] = asp_exchange[idx][0]
        if len(asp) == 4 and asp[3] != "NULL":
            phrases_dict[asp[3]] = asp_exchange[idx][3]
    
    
    phrases = [tup[0] for tup in asp_current if tup[0] != "NULL"]
    if len(asp_current[0]) == 4:
        phrases += [tup[3] for tup in asp_current if tup[3] != "NULL"]
        
    
    phrases = list(set(phrases))
    # sort phrases by length (prio 1) and alphabetically (prio 2)
    phrases.sort(key=lambda x: (len(x), x))
    phrases.reverse()
    
    for phrase in phrases:
        text = text.replace(phrase, phrases_dict[phrase])
        
    for gph in phrases_dict.values():
        if not(gph in text):
            print("Warning: The phrase " + gph + " is not in the text ", text)
            if returnFalseError:
                return False

    return text

def extract_array_from_string(predicted_label):
    match = re.search(r"\[(.*\])", predicted_label)
    if match:
        return match.group(0)
    else:
        return None

def to_pred_list(text, n_elements):
    text_original = text
    text = text[text.find("[") :][1:]
    text = "[" + text
    text = text.replace("\n", "")

    text = re.sub(r"\[ *\( *[\'\"]", "", text)
    text = re.sub(r"[\"\'] *, *[\'\"]", "#####", text)
    text = re.sub(r"[\"\']\) *, *\([\"\']", "#####", text)
    text = re.sub(r"[\"\'] *\) *\]", "", text)
    matches = text.split("#####")
    matches = [match.strip() for match in matches]
    label = []
    for i in range(0, len(matches), n_elements):
        if len(matches[i : i + n_elements]) != n_elements:
            raise ValueError(f"Error in text: {text_original}")
        label.append(matches[i : i + n_elements])

    return label

def validate_label(predicted_label, input_text, unique_aspect_categories, polarities=["positive", "negative", "neutral"], task="asqp", is_string=True, allow_small_variations=False, check_unique_ac=True):
        if is_string:
          predicted_label = extract_array_from_string(predicted_label)
          if predicted_label == None:
            return [False, "no list in prediction"]
        
          try:
            label = eval(predicted_label)
          except:
            return [False, "no list in prediction"]

        else:
           label = predicted_label
        
        # 1. Check if the parsed object is a list
        try:
           if not isinstance(label, list):
              return [False, "not a list"]
        except:
           return [False, "not a list"]
        
        # 2. Check if the list contains exactly min one tuple
        if len(label) < 1:
            return [False, "no tuple found"]
        
        # 3. Check if the single element in the list is a tuple
        for element in label:
          if not isinstance(element, tuple):
             return [False, "inner elements not of type tuple"]
        
        # 4. Check if each element in the array is a tuple with exactly k elements
        n_elements_task = {"asqp": 4, "tasd": 3}
        for aspect in label:
          if len(aspect) != n_elements_task[task]:
              return [False, f"tuple has not exactly {n_elements_task[task]} elements"]
          
          for idx, item in enumerate(aspect):
            if not isinstance(item, str):
                return [False, "sentiment element not of type string"]
            
            # Check if sentiment element is empty string
            if len(item) < 1:
                return [False, "sentiment element string is empty string"]
            
            # Check if the 3rd value of the tuple is either 'positive', 'negative', or 'neutral'
            if item not in polarities and idx == 2:
                return [False, f"item {item} not a sentiment"]
            
            # Check if the category (2nd value) is in unique_aspect_categories
            if item not in unique_aspect_categories and idx == 1 and check_unique_ac == True:
                return [False, f"item {item} is not a correct aspect category"]
            
        # 5. Check if the terms are in sentence
        if allow_small_variations == True:
            new_label = []
            for tup in label:
                tup = list(tup)  # Convert to list to allow modifications

                # Case 1: Handle aspect term variation or capitalization
                if tup[0] != "NULL" and tup[0].lower() not in input_text.lower():
                    if check_if_similar_phrase_exists(tup[0], input_text) == False:
                        return [False, "aspect term not in text"]
                    else:
                        tup[0] = check_if_similar_phrase_exists(tup[0], input_text)

                # Case 2: Aspect term in text but different capitalization
                elif tup[0] != "NULL" and tup[0].lower() in input_text.lower():
                    start = input_text.lower().index(tup[0].lower())
                    end = start + len(tup[0])
                    tup[0] = input_text[start:end]

                elif tup[0] != "NULL" and tup[0].lower() not in input_text.lower():
                    return [False, "aspect term not in text"]

                # Check opinion term (element 4) if task is ASQP
                if task == "asqp":
                    if tup[3] != "NULL" and tup[3].lower() not in input_text.lower():
                        if check_if_similar_phrase_exists(tup[3], input_text) == False:
                            return [False, "opinion term not in text"]
                        else:
                            tup[3] = check_if_similar_phrase_exists(tup[3], input_text)
                    elif tup[3] != "NULL" and tup[3].lower() in input_text.lower():
                        start = input_text.lower().index(tup[3].lower())
                        end = start + len(tup[3])
                        tup[3] = input_text[start:end]
                    elif tup[3] != "NULL" and tup[3].lower() not in input_text.lower():
                        return [False, "opinion term not in text"]

                new_label.append(tuple(tup))  # Convert back to tuple

            label = new_label  # aktualisierte Liste übernehmen

        else: 
           # 5. Check if terms are in sentence
           for _tuple in label:
               if not (_tuple[0] in input_text) and _tuple[0] != "NULL": 
                   return [False, "aspect term not in text"]
               if task == "asqp":
                  if not (_tuple[3] in input_text) and _tuple[3] != "NULL": 
                      return [False, "opinion term not in text"]
  
        
        label = [tuple([t.strip() for t in tup]) for tup in label]
        # 6. If all checks pass, return the array
        return [label]
    
def validate_reasoning(output):
    if len(output) == 0:
        return [False, "no text found"]

    return [True]


all_chars = string.ascii_letters + string.digits + "äöüÄÖÜßàâçéèêëîïôûùüáéíóúüñàèéìíóòùáčďéěíňóřšťúůýžáéëïóöüабвгдеёжзийклмнопрстуфхцчшщыэюя" + "çğıöşü"

def check_if_similar_phrase_exists(phrase, text_gen):
    # Überprüfen, ob die Phrase eine ähnliche Phrase im Text mit einer maximalen Veränderung von 1 Zeichen hat
    for i in range(len(phrase)):
        for char in all_chars:  # Verwenden des langen Alphabets
            modified_phrase = phrase[:i] + char + phrase[i+1:]
            if modified_phrase in text_gen:
                return modified_phrase
    return False

def validate_translation(txt_gen, gold_label, text_original, task="tasd"):
    txt_gen = txt_gen.replace("```", "").replace("\n", "").replace("\`", "")
    
    if "<0x" in txt_gen:
        return False

    task_tuple_length = {
        "tasd": 3,
        "asqp": 4,
    }
    if "####" not in txt_gen:
        return False

    
    try:
        label_gen = to_pred_list(txt_gen.split("####")[1], n_elements=task_tuple_length[task])
        label_gen = [tuple([el for el in t]) for t in label_gen]
        text_gen = txt_gen.split("####")[0]
    except:
        return False
    
    text_gen = text_gen.strip()

    try:
        if type(label_gen[0]) != tuple:
            return False
        label_gen = [[el.strip() for el in t] for t in label_gen]
    except:
        return False

    if len(label_gen) != len(gold_label):
        return False

    for tup in label_gen:
        if len(tup) != task_tuple_length[task]:
            return False
        
    for tup_idx, tup in enumerate(label_gen):
        if tup[0] != "NULL" and gold_label[tup_idx][0] == "NULL":
            return False
        if task == "asqp":
            if tup[3] != "NULL" and gold_label[tup_idx][3] == "NULL":
                return False
    for tup_idx, tup in enumerate(label_gen):
        if tup[0] == "" or tup[0] == " ":
            return False
        if task == "asqp":
            if tup[3] == "" or tup[3] == " ":
                return False

    for tup in label_gen:
        # 1. Fall nur 1 character unterschied tup[0] und phrase in text_gen
        if tup[0] != "NULL" and tup[0].lower() not in text_gen.lower():
            if check_if_similar_phrase_exists(tup[0], text_gen) == False:
                return False
            else:
                tup[0] = check_if_similar_phrase_exists(tup[0], text_gen)
        # 2. Fall tup[0] ist in text_gen allerdigns mit anderen caps
        elif tup[0] != "NULL" and tup[0].lower() in text_gen.lower():
            start = text_gen.lower().index(tup[0].lower())
            end = start + len(tup[0])
            tup[0] = text_gen[start:end]    
        elif tup[0] != "NULL" and tup[0].lower() not in text_gen.lower():
            return False   
        
        if task == "asqp":
            if tup[3] != "NULL" and tup[3].lower() not in text_gen.lower():
                if check_if_similar_phrase_exists(tup[3], text_gen) == False:
                    return False
                else:
                    tup[3] = check_if_similar_phrase_exists(tup[3], text_gen)
            elif tup[3] != "NULL" and tup[3].lower() in text_gen.lower():
                start = text_gen.lower().index(tup[3].lower())
                end = start + len(tup[3])
                tup[3] = text_gen[start:end]    
            elif tup[3] != "NULL" and tup[3].lower() not in text_gen.lower():
                return False
    
    for tup in label_gen:
        if tup[0] != "NULL" and tup[0] not in text_gen:
            raise KeyboardInterrupt("Owaia")


    for tup in label_gen:
        if re.search(r"\b" + re.escape(tup[0]) + r"\b", text_gen) is None and tup[0] != "NULL":
            return False
        if task == "asqp":
            if re.search(r"\b" + re.escape(tup[3]) + r"\b", text_gen) is None and tup[3] != "NULL":
                return False
            
    # check if exchange of label and aspect is possible
    if exchange_phrases(label_gen, gold_label, text_gen, returnFalseError=True) == False:
        return False
    
    if exchange_phrases(gold_label, label_gen, text_original, returnFalseError=True) == False:
        return False


    for idx, tup in enumerate(gold_label):
        label_gen[idx][1] = tup[1]
        label_gen[idx][2] = tup[2]

    return [tuple(l) for l in label_gen], text_gen


