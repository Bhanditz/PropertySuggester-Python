from StringIO import StringIO

from testtools import TestCase

from propertysuggester.parser import CsvReader
from propertysuggester.test.parser.test_abstract_reader import AbstractUniverseTest


class CsvReaderTest(AbstractUniverseTest):
    def test_universe(self):
        out = StringIO()
        out.writelines(["Q1,claim,373,string,Universe\n",
                        "Q1,reference,143,wikibase-entityid,Q328\n"
                        "Q1,claim,31,wikibase-entityid,Q223557\n",
                        "Q1,claim,31,wikibase-entityid,Q1088088\n",
                        "Q1,claim,361,wikibase-entityid,Q3327819\n",
                        "Q1,qualifier,31,wikibase-entityid,Q41719\n"])
        out.seek(0)
        result = list(CsvReader.read_csv(out))

        self.assert_universe(result)

class CsvReaderTest2(TestCase):
    def test_invalid_row_throws_exception(self):
        f = StringIO()
        f.writelines(["a,b"])
        f.seek(0)

        self.assertRaises(ValueError, lambda: list(CsvReader.read_csv(f)))
