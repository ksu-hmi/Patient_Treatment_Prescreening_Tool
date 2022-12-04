class Illness:

# Removed flu_score and allergy_score 
    def __init__(self):
        self._cold_score = 0
        self._covid_score = 0
        

# Added symptoms to match those in symptoms dataset
    def ask_questions(self):
        self.fever()
        self.headache()
        self.body_aches()
        self.fatigue()
        self.congestion()
        self.sneezing()
        self.sore_throat()
        self.cough()
        self.shortness_breath()
        self.runny_nose()
        self.diarrhea()
        self.scratchy_throat()
        self.watery_eyes()
        self.nausea()
        self.vomiting()
        self.lost_smell_or_taste()
        self.chills()
        self.sinus_pressure()
        self.score()
        return True

# Removed flu and allergy scores from each function 
# Defined each symptom on our dataset, an input variable for each symptom, and a score variable that is based on user input

    def fever(self):
        """ Asks if they have a fever """
        #Altered fever output message
        fever_input = input("Do you have a fever with a temperature of 100F or greater? (y/n): ")

        # checking for valid answer
        if fever_input.lower() != 'y' and fever_input.lower() != 'n':
            print('Invalid answer')
            self.fever()

        # increase score if the symptom is present
        elif fever_input.lower() == 'y':
            self._covid_score += 10
            self._cold_score += 0

    def headache(self):
        """Asks if they have a headache"""

        headache_input = input("Do you have a headache? (y/n): ")

        if headache_input.lower() != 'y' and headache_input.lower() != 'n':
            print('Invalid answer')
            self.headache()

        elif headache_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 1

    def body_aches(self):
        """ Ask if they have body or muscle aches"""

        pain_input = input('Do you have any body or muscle aches? (y/n): ')

        if pain_input.lower() != 'y' and pain_input.lower() != 'n':
            print('Invalid answer')
            self.pain()

        elif pain_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 1
            
    def fatigue(self):
        """ Ask if they have fatigue """

        fatigue_input = input('Do you have any fatigue? (y/n): ')

        if fatigue_input.lower() != 'y' and fatigue_input.lower() != 'n':
            print('Invalid answer')
            self.fatigue()

        elif fatigue_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 1

    def congestion(self):
        """ Ask if they have congestion"""

        stuffy_nose_input = input('Do you have a stuffy nose or congestion? (y/n): ')

        if stuffy_nose_input.lower() != 'y' and stuffy_nose_input.lower() != 'n':
            print('Invalid answer')
            self.stuffy_nose()

        elif stuffy_nose_input.lower() == 'y':
            self._cold_score += 1
            self._cold_score += 10

    def sneezing(self):
        """ Ask if they are sneezing """

        sneezing_input = input('Do you have a lot of sneezing? (y/n): ')

        if sneezing_input.lower() != 'y' and sneezing_input.lower() != 'n':
            print('Invalid answer, try again')
            self.sneezing()

        elif sneezing_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 10

    def sore_throat(self):
        """ Ask if they have a sore throat """

        sore_throat_input = input('Do you have a sore throat? (y/n): ')

        if sore_throat_input.lower() != 'y' and sore_throat_input.lower() != 'n':
            print('Invalid answer, try again')
            self.sore_throat()

        elif sore_throat_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 10

    def cough(self):
        """ Ask if they have a cough"""

        cough_input = input('Do you have the coughs? (y/n): ')

        if cough_input.lower() != 'y' and cough_input.lower() != 'n':
            print('Invalid answer, try again')
            self.cough()

        elif cough_input.lower() == 'y':
            self._covid_score += 10
            self._cold_score += 5

    def shortness_breath(self):
        """ Ask if they have shortness of breath """

        breath_input = input('Do you have shortness of breath? (y/n): ')

        if breath_input.lower() != 'y' and breath_input.lower() != 'n':
            print('Invalid answer, try again')
            self.shortness_breath()

        elif breath_input.lower() == 'y':
            self._covid_score += 10
            self._cold_score += 1

    def runny_nose(self):
        """ Ask if they have runny nose """

        runny_nose_input = input('Do you have a runny nose (y/n): ')

        if runny_nose_input.lower() != 'y' and runny_nose_input.lower() != 'n':
            print('Invalid answer, try again')
            self.runny_nose()

        elif runny_nose_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 10

    def diarrhea(self):
        """ Ask if they have diarrhea """

        diarrhea_input = input('Do you have diarrhea? (y/n): ')

        if diarrhea_input.lower() != 'y' and diarrhea_input != 'n':
            print('Invalid answer, try again')
            self.diarrhea()

        elif diarrhea_input.lower() == 'y':
            self._covid_score += 10
            self._cold_score += 1

        else:
            pass
    
# Defined symptom and user input variables for each 
    def scratchy_throat(self):
        """ Ask if they have a scratchy throat """

        scratchy_throat_input = input('Do you have a scratchy throat? (y/n): ')

        if scratchy_throat_input.lower() != 'y' and scratchy_throat_input.lower() != 'n':
            print('Invalid answer')
            self.scratchy_throat()

        elif scratchy_throat_input.lower() == 'y':
            self._covid_score += 2
            self._cold_score += 5

    def watery_eyes(self):
        """ Ask if they have watery eyes """

        watery_eyes_input = input('Do you have watery eyes? (y/n): ')

        if watery_eyes_input.lower() != 'y' and watery_eyes_input.lower() != 'n':
            print('Invalid answer')
            self.watery_eyes()

        elif watery_eyes_input.lower() == 'y':
            self._covid_score += 0
            self._cold_score += 2

    def nausea(self):
        """ Ask if they have nausea """

        nausea_input = input('Do you have nausea? (y/n): ')

        if nausea_input.lower() != 'y' and nausea_input.lower() != 'n':
            print('Invalid answer')
            self.nausea()

        elif nausea_input.lower() == 'y':
            self._covid_score += 3
            self._cold_score += 1

    def vomiting(self):
        """ Ask if they have been vomiting """

        vomiting_input = input('Have you thrown up? (y/n): ')

        if vomiting_input.lower() != 'y' and vomiting_input.lower() != 'n':
            print('Invalid answer')
            self.vomiting()

        elif vomiting_input.lower() == 'y':
            self._covid_score += 3
            self._cold_score += 1

    def lost_smell_or_taste(self):
        """ Ask if they have lost their smell or taste """

        lost_input = input('Have you lost your smell or taste? (y/n): ')

        if lost_input.lower() != 'y' and lost_input.lower() != 'n':
            print('Invalid answer')
            self.lost_smell_or_taste()

        elif lost_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 0

    def chills(self):
        """ Ask if they have experienced chills """

        chills_input = input('Have you experienced chills? (y/n): ')

        if chills_input.lower() != 'y' and chills_input.lower() != 'n':
            print('Invalid answer')
            self.chills()

        elif chills_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 2

    def sinus_pressure(self):
        """ Ask if they have sinus pressure """

        sp_input = input('Do you have sinus pressure? (y/n): ')

        if sp_input.lower() != 'y' and sp_input.lower() != 'n':
            print('Invalid answer')
            self.sinus_pressure()

        elif sp_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 3

    def score(self):
        scores = []
        scores.append(int(self._covid_score))
        scores.append(int(self._cold_score))
        scores.sort()

# Changed output messages 
        print('\nBased on our findings with your symptoms, we think your symtoms are most likely related to the following: ')

        if scores[-1] == self._cold_score:
            print('It may seem like you are experiencing a cold')
            print('There are a few Over The Counter medications that you are able to take') #insert a medical comment on medications
            print() #insert OTC medications individually with information on medications
        elif scores[-1] == self._covid_score:
            print ('Covid-19: Please quarantine until tested and you have recieved a negative result. In addition, contact your doctor as soon as possible.')

        print('\n')
        print('\nNote that these findings are from http://www.kdheks.gov/coronavirus/toolkit/Cold_vs._Flu_vs._Allergies_vs._Coronavirus.pdf')
        print('For an accurate representation, we recommend consulting with a doctor.')



if __name__ == '__main__':
    il = Illness()
    il.ask_questions()