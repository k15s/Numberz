class NumberService(object):

    """Service to translate English number expressions to integer friendly
    format"""

    def __init__(self):
        """Initialize helper dictionaries that map from English to ints"""

        # single digits in English have their own handler, e.g. 'one thousand'
        self.singles_and_doubles = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90
        }

        self.trailing_zeroes = {
            'hundred':      100,
            'thousand':     1000,
            'million':      1000000,
            'billion':      1000000000,
            'trillion':     1000000000000,
        }

        # set for keywords
        self.addition_keywords = {'and', 'plus'}

    def parse_english(self, input):
        """
        Parse an English expression of a single number. The expression has to
        be entirely in English - no mixture of digits. Input is an english
        string separated by single spaces.

        We split the english number into portions and handle them separately,
        so we have a running sum for the work/values of each portion, separate
        from each other.

        EXAMPLES:
        one hundred fifty six thousand two hundred twelve = 156,000 + 212

        one hundred million one thousand one hundred one = 100,000,000 + 1000 +
        101

        After every trailing zero expression of 'thousand' or higher, we add
        the current running sum to the total sum then reset the running sum for
        the next expression. This way we build the number up via addition.
        """
        input = input.lower()
        print "parsing english input: " + input

        # handle already digit-formatted input
        try:
            result = float(input)
            print "result: " + str(result)
            return result
        except Exception:
            pass

        sp = input.split(" ")

        running_sum = 0
        acc = 0  # the total accumulated number
        sign = 1
        for val in sp:
            print ("parsing " + str(val) + ", running sum: " + str(running_sum) + \
                   ", acc: " + str(acc))
            if val == 'negative':
                sign *= -1
            else:
                digit = self.singles_and_doubles.get(val, None)
                trailing_zeroes = self.trailing_zeroes.get(val, None)
                # standard digit, add to running_sum - note that None and 0 are
                # the 'same' in conditional, so distinguish
                if digit is 0 or digit is not None:
                    running_sum += sign * digit
                elif trailing_zeroes:
                    # special case: whenever we find 'hundred' we can multiply
                    # our running sum by 100 and continue, as hundred is always
                    # followed by more digits that are added to running sum or
                    # larger trailing zeroes that are multiplied by running sum
                    if trailing_zeroes == 100:
                        running_sum *= 100
                    # whenever we see 'thousand', 'million', etc. running_sum
                    # is plain digits or '___ hundred ___' so we always
                    # multiply running value by the trailing zeroes in these
                    # cases then reset running_sum to avoid compounding
                    # trailing zeroes with each other, e.g. we don't want to
                    # multiply 1 million by 1 thousand in 1,001,000
                    else:
                        acc += running_sum * trailing_zeroes
                        running_sum = 0
                else:
                    raise Exception("UnrecognizedInput")

        # add last running_sum, if any, to accumulator
        acc += running_sum
        print "Returning acc: " + str(acc) + "\n"
        return acc
