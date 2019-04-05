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
from .. import delete_dataset
from .. import get_dataset
from .. import list_datasets
from .. import update_dataset_description
from .. import update_dataset_default_table_expiration
from .. import update_dataset_access


def test_dataset_samples(capsys, client, random_dataset_id):

    # create dataset
    create_dataset.create_dataset(client, random_dataset_id)
    out, err = capsys.readouterr()
    assert "Created dataset {}".format(random_dataset_id) in out

    # get dataset
    get_dataset.get_dataset(client, random_dataset_id)
    out, err = capsys.readouterr()
    assert random_dataset_id in out

    # list dataset
    list_datasets.list_datasets(client)
    out, err = capsys.readouterr()
    assert "Datasets in project {}:".format(client.project) in out

    # update dataset description
    update_dataset_description.update_dataset_description(client, random_dataset_id)
    out, err = capsys.readouterr()
    assert "Updated description." in out

    # update dataset table expiration
    update_dataset_default_table_expiration.update_dataset_default_table_expiration(
        client, random_dataset_id
    )
    out, err = capsys.readouterr()
    assert "Updated dataset {}".format(random_dataset_id) in out

    # update dataset permissions
    update_dataset_access.update_dataset_access(client, random_dataset_id)
    out, err = capsys.readouterr()
    assert (
        "Updated dataset '{}' with modified user permissions.".format(random_dataset_id)
        in out
    )

    # delete dataset
    delete_dataset.delete_dataset(client, random_dataset_id)
    out, err = capsys.readouterr()
    assert "Deleted dataset '{}'.".format(random_dataset_id) in out
