# -*- coding: utf-8 -*-
# Copyright 2014-2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import unittest

from synapse.rest.media.v1.preview_url_resource import summarize_paragraphs


class PreviewTestCase(unittest.TestCase):

    def test_long_summarize(self):
        example_paras = [
            """Tromsø (Norwegian pronunciation: [ˈtrʊmsœ] ( listen); Northern Sami:
            Romsa; Finnish: Tromssa[2] Kven: Tromssa) is a city and municipality in
            Troms county, Norway. The administrative centre of the municipality is
            the city of Tromsø. Outside of Norway, Tromso and Tromsö are
            alternative spellings of the city.Tromsø is considered the northernmost
            city in the world with a population above 50,000. The most populous town
            north of it is Alta, Norway, with a population of 14,272 (2013).""",

            """Tromsø lies in Northern Norway. The municipality has a population of
            (2015) 72,066, but with an annual influx of students it has over 75,000
            most of the year. It is the largest urban area in Northern Norway and the
            third largest north of the Arctic Circle (following Murmansk and Norilsk).
            Most of Tromsø, including the city centre, is located on the island of
            Tromsøya, 350 kilometres (217 mi) north of the Arctic Circle. In 2012,
            Tromsøya had a population of 36,088. Substantial parts of the urban area
            are also situated on the mainland to the east, and on parts of Kvaløya—a
            large island to the west. Tromsøya is connected to the mainland by the Tromsø
            Bridge and the Tromsøysund Tunnel, and to the island of Kvaløya by the
            Sandnessund Bridge. Tromsø Airport connects the city to many destinations
            in Europe. The city is warmer than most other places located on the same
            latitude, due to the warming effect of the Gulf Stream.""",

            """The city centre of Tromsø contains the highest number of old wooden
            houses in Northern Norway, the oldest house dating from 1789. The Arctic
            Cathedral, a modern church from 1965, is probably the most famous landmark
            in Tromsø. The city is a cultural centre for its region, with several
            festivals taking place in the summer. Some of Norway's best-known
             musicians, Torbjørn Brundtland and Svein Berge of the electronica duo
             Röyksopp and Lene Marlin grew up and started their careers in Tromsø.
             Noted electronic musician Geir Jenssen also hails from Tromsø.""",
        ]

        desc = summarize_paragraphs(example_paras, min_size=200, max_size=500)

        self.assertEquals(
            desc,
            "Tromsø (Norwegian pronunciation: [ˈtrʊmsœ] ( listen); Northern Sami:"
            " Romsa; Finnish: Tromssa[2] Kven: Tromssa) is a city and municipality in"
            " Troms county, Norway. The administrative centre of the municipality is"
            " the city of Tromsø. Outside of Norway, Tromso and Tromsö are"
            " alternative spellings of the city.Tromsø is considered the northernmost"
            " city in the world with a population above 50,000. The most populous town"
            " north of it is Alta, Norway, with a population of 14,272 (2013)."
        )

        desc = summarize_paragraphs(example_paras[1:], min_size=200, max_size=500)

        self.assertEquals(
            desc,
            "Tromsø lies in Northern Norway. The municipality has a population of"
            " (2015) 72,066, but with an annual influx of students it has over 75,000"
            " most of the year. It is the largest urban area in Northern Norway and the"
            " third largest north of the Arctic Circle (following Murmansk and Norilsk)."
            " Most of Tromsø, including the city centre, is located on the island of"
            " Tromsøya, 350 kilometres (217 mi) north of the Arctic Circle. In 2012,"
            " Tromsøya had a population of 36,088. Substantial parts of the…"
        )

    def test_short_summarize(self):
        example_paras = [
            "Tromsø (Norwegian pronunciation: [ˈtrʊmsœ] ( listen); Northern Sami:"
            " Romsa; Finnish: Tromssa[2] Kven: Tromssa) is a city and municipality in"
            " Troms county, Norway.",

            "Tromsø lies in Northern Norway. The municipality has a population of"
            " (2015) 72,066, but with an annual influx of students it has over 75,000"
            " most of the year.",

            "The city centre of Tromsø contains the highest number of old wooden"
            " houses in Northern Norway, the oldest house dating from 1789. The Arctic"
            " Cathedral, a modern church from 1965, is probably the most famous landmark"
            " in Tromsø.",
        ]

        desc = summarize_paragraphs(example_paras, min_size=200, max_size=500)

        self.assertEquals(
            desc,
            "Tromsø (Norwegian pronunciation: [ˈtrʊmsœ] ( listen); Northern Sami:"
            " Romsa; Finnish: Tromssa[2] Kven: Tromssa) is a city and municipality in"
            " Troms county, Norway.\n"
            "\n"
            "Tromsø lies in Northern Norway. The municipality has a population of"
            " (2015) 72,066, but with an annual influx of students it has over 75,000"
            " most of the year."
        )

    def test_small_then_large_summarize(self):
        example_paras = [
            "Tromsø (Norwegian pronunciation: [ˈtrʊmsœ] ( listen); Northern Sami:"
            " Romsa; Finnish: Tromssa[2] Kven: Tromssa) is a city and municipality in"
            " Troms county, Norway.",

            "Tromsø lies in Northern Norway. The municipality has a population of"
            " (2015) 72,066, but with an annual influx of students it has over 75,000"
            " most of the year."
            " The city centre of Tromsø contains the highest number of old wooden"
            " houses in Northern Norway, the oldest house dating from 1789. The Arctic"
            " Cathedral, a modern church from 1965, is probably the most famous landmark"
            " in Tromsø.",
        ]

        desc = summarize_paragraphs(example_paras, min_size=200, max_size=500)
        self.assertEquals(
            desc,
            "Tromsø (Norwegian pronunciation: [ˈtrʊmsœ] ( listen); Northern Sami:"
            " Romsa; Finnish: Tromssa[2] Kven: Tromssa) is a city and municipality in"
            " Troms county, Norway.\n"
            "\n"
            "Tromsø lies in Northern Norway. The municipality has a population of"
            " (2015) 72,066, but with an annual influx of students it has over 75,000"
            " most of the year. The city centre of Tromsø contains the highest number"
            " of old wooden houses in Northern Norway, the oldest house dating from"
            " 1789. The Arctic Cathedral, a modern church…"
        )
