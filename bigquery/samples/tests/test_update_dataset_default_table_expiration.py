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

from .. import create_dataset
from .. import update_dataset_default_table_expiration


def test_update_dataset_default_table_expiration(
    capsys, client, random_dataset_id, one_day_ms
):

    create_dataset.create_dataset(client, random_dataset_id)

    update_dataset_default_table_expiration.update_dataset_default_table_expiration(
        client, random_dataset_id, one_day_ms
    )
    out, err = capsys.readouterr()
    assert (
        "Updated dataset {} with new expiration {}".format(
            random_dataset_id, one_day_ms
        )
        in out
    )
