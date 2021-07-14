import unittest
class TestNewModel(unittest.TestCase):
    def generic_test(self):
        b=4
        assert(b==4)
def main(): 

        suite = unittest.defaultTestLoader.loadTestsFromModule(TestNewModel())
    
        runner = unittest.TextTestRunner()
        result = runner.run (suite)
        print('Successful : ',result.wasSuccessful())

        return result.wasSuccessful()
if __name__ == '__main__':

    main()