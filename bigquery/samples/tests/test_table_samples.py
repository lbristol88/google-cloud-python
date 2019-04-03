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
from .. import list_tables
from .. import get_table
from .. import delete_table


def test_table_samples(capsys, client, random_table_id, dataset_id):

    create_table.create_table(client, random_table_id)
    out, err = capsys.readouterr()
    assert "Created table {}".format(random_table_id) in out

    list_tables.list_tables(client, dataset_id)
    out, err = capsys.readouterr()
    assert "Tables contained in '{}':".format(dataset_id) in out

    get_table.get_table(client, random_table_id)
    out, err = capsys.readouterr()
    assert random_table_id in out

    delete_table.delete_table(client, random_table_id)
    out, err = capsys.readouterr()
    assert "Deleted table '{}'.".format(random_table_id) in out
