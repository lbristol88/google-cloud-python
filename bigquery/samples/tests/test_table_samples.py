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


def test_table_samples(capsys, client, project_id, dataset_id, table_id):
    """Since creating a table is a long operation, test all table model samples
    in the same test, following a typical end-to-end flow.
    """
    create_table.create_table(client, project_id, dataset_id, table_id)
    out, err = capsys.readouterr()
    assert create_table in out
    assert table.table_id == "my_table"
