class Illness:

    def __init__(self):
        self._flu_score = 0
        self._cold_score = 0
        self._covid_score = 0
        self._allergy_score = 0


    def ask_questions(self):
        self.fever()
        self.headache()
        self.pain()
        self.extreme_exhaustion()
        self.stuffy_nose()
        self.sneezing()
        self.sore_throat()
        self.cough()
        self.shortness_breath()
        self.runny_nose()
        self.diarrhea()
        self.score()
        return True


    def fever(self):
        """ Asks if they have a fever """

        fever_input = input("Do you have a fever with a temperature of at least 100F (y/n): ")

        # checking for valid answer
        if fever_input.lower() != 'y' and fever_input.lower() != 'n':
            print('Invalid answer')
            self.fever()

        # increase score if the symptom is present
        elif fever_input.lower() == 'y':
            self._covid_score += 10
            self._flu_score += 10

    def headache(self):
        """Asks if they have a headache"""

        headache_input = input("Do you have a headache? (y/n): ")

        if headache_input.lower() != 'y' and headache_input.lower() != 'n':
            print('Invalid answer')
            self.headache()

        elif headache_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 1
            self._flu_score += 10
            self._allergy_score += 5


    def pain(self):
        """ Ask if they have pain """

        pain_input = input('Do you have any general pain around your body? (y/n): ')

        if pain_input.lower() != 'y' and pain_input.lower() != 'n':
            print('Invalid answer')
            self.pain()

        elif pain_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 1
            self._flu_score += 10


    def fatigue(self):
        """ Ask if they have fatigue """

        fatigue_input = input('Do you have any fatigue? (y/n): ')

        if fatigue_input.lower() != 'y' and fatigue_input.lower() != 'n':
            print('Invalid answer')
            self.fatigue()

        elif fatigue_input.lower() == 'y':
            self._covid_score += 5
            self._cold_score += 1
            self._flu_score += 10
            self._allergy_score += 5

    def extreme_exhaustion(self):
        """ Ask if they have extreme exhaustion """

        exhaustion_input = input('Do you have extreme exhaustion? (y/n): ')

        if exhaustion_input.lower() != 'y' and exhaustion_input.lower() != 'n':
            print('Invalid answer')
            self.extreme_exhaustion()

        elif exhaustion_input.lower() == 'y':
            self._covid_score += 5
            self._flu_score += 10


    def stuffy_nose(self):
        """ Ask if they have a stuffy nose"""

        stuffy_nose_input = input('Do you have a stuffy nose? (y/n): ')

        if stuffy_nose_input.lower() != 'y' and stuffy_nose_input.lower() != 'n':
            print('Invalid answer')
            self.stuffy_nose()

        elif stuffy_nose_input.lower() == 'y':
            self._cold_score += 1
            self._cold_score += 10
            self._flu_score += 5
            self._allergy_score += 10


    def sneezing(self):
        """ Ask if they are sneezing """

        sneezing_input = input('Do you have a lot of sneezing? (y/n): ')

        if sneezing_input.lower() != 'y' and sneezing_input.lower() != 'n':
            print('Invalid answer, try again')
            self.sneezing()

        elif sneezing_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 10
            self._flu_score += 5
            self._allergy_score += 10



    def sore_throat(self):
        """ Ask if they have a sore throat """

        sore_throat_input = input('Do you have a sore throat? (y/n): ')

        if sore_throat_input.lower() != 'y' and sore_throat_input.lower() != 'n':
            print('Invalid answer, try again')
            self.sore_throat()

        elif sore_throat_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 10
            self._flu_score += 10

    def cough(self):
        """ Ask if they have a cough"""

        cough_input = input('Do you have the coughs? (y/n): ')

        if cough_input.lower() != 'y' and cough_input.lower() != 'n':
            print('Invalid answer, try again')
            self.cough()

        elif cough_input.lower() == 'y':
            self._covid_score += 10
            self._cold_score += 5
            self._flu_score += 10
            self._allergy_score += 5

    def shortness_breath(self):
        """ Ask if they have shortness of breath """

        breath_input = input('Do you have shortness of breath? (y/n): ')

        if breath_input.lower() != 'y' and breath_input.lower() != 'n':
            print('Invalid answer, try again')
            self.shortness_breath()

        elif breath_input.lower() == 'y':
            self._covid_score += 10
            self._cold_score += 1
            self._flu_score += 1
            self._allergy_score += 10

    def runny_nose(self):
        """ Ask if they have runny nose """

        runny_nose_input = input('Do you have a runny nose (y/n): ')

        if runny_nose_input.lower() != 'y' and runny_nose_input.lower() != 'n':
            print('Invalid answer, try again')
            self.runny_nose()

        elif runny_nose_input.lower() == 'y':
            self._covid_score += 1
            self._cold_score += 10
            self._flu_score += 5
            self._allergy_score += 10

    def diarrhea(self):
        """ Ask if they have diarrhea """

        diarrhea_input = input('Do you have diarrhea? (y/n): ')

        if diarrhea_input.lower() != 'y' and diarrhea_input != 'n':
            print('Invalid answer, try again')
            self.diarrhea()

        elif diarrhea_input.lower() == 'y':
            self._covid_score += 10
            self._flu_score += 5

        else:
            pass

    def score(self):
        scores = []
        scores.append(int(self._flu_score))
        scores.append(int(self._covid_score))
        scores.append(int(self._cold_score))
        scores.append(int(self._allergy_score))
        scores.sort()


        print('\nBased on our findings with your symptoms, we think you are mostly associated with this kind of symptom: ')

        if scores[-1] == self._flu_score:
            print('Flu')

        elif scores[-1] == self._covid_score:
            print('Corona Virus')

        elif scores[-1] == self._cold_score:
            print('Cold')

        else:
            print('Allergy')

        print('\n')

        print("Another potential could be: ")
        if scores[-2] == self._flu_score:
            print('Flu')
        elif scores[-2] == self._cold_score:
            print('Corona Virus')
        elif scores[-2] == self._cold_score:
            print('Cold')
        else:
            print('Allergy')

        print('\nNote that these findings are from http://www.kdheks.gov/coronavirus/toolkit/Cold_vs._Flu_vs._Allergies_vs._Coronavirus.pdf')
        print('For an accurate representation, we recommend consulting with a doctor.')


if __name__ == '__main__':
    il = Illness()
    il.ask_questions()



