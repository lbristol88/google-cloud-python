# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .. import create_table
from .. import get_table


def test_get_table(capsys, client, table_id):

    get_table.get_table(client, table_id)
    out, err = capsys.readouterr()
    assert "Got table '{}'.".format(table_id) in out
    assert "full_name" in out  # test that schema is printed
    assert "Table description: Sample Table" in out
    assert "Table has 0 rows" in out
