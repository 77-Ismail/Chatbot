import random
R_JOKE = "What do a tick and the Eiffel tower have in common? They’re both Paris sites"
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_PYTHON_ROADMAP = "1- Basics of Python\n     2- Data Structures\n     3- Modules and Libraries\n     4- File Handling and Input/Output\n     5- Object-Oriented Programming\n     6- Error Handling and Exceptions Regular."

R_AGRICULTURE = """Agriculture is the practice of cultivating plants, animals, and other organisms for food,fiber, medicinal plants, and other products used to sustain and enhance human life."""
#Questions Related to Agriculture (Dataset) -------------------------------------------------------------------------------------------------------------
R_QUESTION_1 = "To improve soil fertility, incorporate organic matter like compost, use cover crops for nutrient cycling, and rotate crops to prevent nutrient depletion."
R_QUESTION_2 = "Natural pest control methods include companion planting, encouraging beneficial insects, and using organic insecticides sparingly."
R_QUESTION_3 = "Determining the right amount of water for plants involves monitoring soil moisture levels, considering plant type and weather conditions, and adjusting irrigation accordingly."
R_QUESTION_4 = """The best crops to grow depend on your specific climate, soil conditions, and market demand. 
                  Research local agricultural resources or consult with agricultural experts for suitable crop recommendations."""
R_QUESTION_5 = "Prevent weeds by employing techniques like mulching to smother weed growth, hand-pulling weeds, or using organic herbicides selectively."
R_QUESTION_6 = """Organic farming emphasizes avoiding synthetic fertilizers and pesticides, relying on sustainable practices like crop rotation and biological pest control, " 
                  and utilizing natural amendments like compost and cover crops."""
R_QUESTION_7 = "Protect crops from diseases by practicing good crop hygiene, implementing proper spacing between plants for air circulation, and selecting disease-resistant crop varieties."
R_QUESTION_8 = "Increasing crop yield can be achieved through soil improvement techniques, precision irrigation methods, optimal nutrient management, and adopting improved crop varieties."
R_QUESTION_9 = "Composting organic waste involves creating a balanced mixture of green and brown materials, maintaining proper moisture and aeration, and turning the compost regularly for decomposition."
R_QUESTION_10 = "Crop rotation benefits include reducing pest and disease pressure, optimizing nutrient utilization, and improving soil health by diversifying crop species grown in a specific area."
R_QUESTION_11 = "Select the right seeds by considering factors such as desired crop characteristics, adaptability to your climate, disease resistance, and seed quality from reputable suppliers."
R_QUESTION_12 = "Sustainable irrigation techniques include using drip or micro-irrigation systems to minimize water waste, employing rainwater harvesting, and practicing efficient scheduling based on plant water needs."
R_QUESTION_13 = "Prevent soil erosion by implementing practices like contour plowing, terracing, mulching, and planting cover crops to stabilize the soil and minimize runoff."
R_QUESTION_14 = "Greenhouse gardening best practices include proper ventilation for temperature control, appropriate spacing between plants, monitoring and adjusting humidity levels, and providing adequate lighting."
R_QUESTION_15 = "Maintaining nutrient balance in a hydroponic system involves regularly monitoring and adjusting the nutrient solution's pH and nutrient concentrations based on plant requirements."
R_QUESTION_16 = "Cover crops offer advantages like reducing soil erosion, suppressing weeds, improving soil fertility, and providing habitat for beneficial insects."
R_QUESTION_17 = "Maximize farm equipment efficiency by ensuring regular maintenance, proper calibration, and appropriate utilization based on the specific tasks and conditions."
R_QUESTION_18 = "Identifying and treating nutrient deficiencies in plants involves observing symptoms, conducting soil or tissue tests, and applying appropriate organic fertilizers or amendments to address deficiencies."
R_QUESTION_19 = "GMOs in agriculture have potential benefits such as increased crop yield and resistance to pests and diseases, but also raise concerns about environmental impact and food safety. Assess the risks and benefits based on scientific research and individual values."
R_QUESTION_20 = "Start a small-scale urban garden by selecting suitable containers or plots, choosing appropriate crops for limited space, ensuring proper sunlight and irrigation, and utilizing vertical gardening techniques."


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
