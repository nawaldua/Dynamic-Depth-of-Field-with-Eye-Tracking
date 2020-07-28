
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



def run_and_save_DAVIS(self, input_, targets, save_path):
    assert (self.num_input == 3)
    input_imgs = autograd.Variable(input_.cuda(), requires_grad=False)

    stack_inputs = input_imgs

    prediction_d, pred_confidence = self.netG.forward(stack_inputs)
    pred_log_d = prediction_d.squeeze(1)
    pred_d = torch.exp(pred_log_d)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i in range(0, len(targets['img_1_path'])):

        youtube_dir = save_path + targets['img_1_path'][i].split('/')[-2]

        if not os.path.exists(youtube_dir):
            os.makedirs(youtube_dir)

        saved_img = np.transpose(
            input_imgs[i, :, :, :].cpu().numpy(), (1, 2, 0))

        pred_d_ref = pred_d.data[i, :, :].cpu().numpy()

        output_path = youtube_dir + '/' + \
            targets['img_1_path'][i].split('/')[-1]
        print(output_path)
        disparity = 1. / pred_d_ref
        disparity = disparity / np.max(disparity)

        ################### EDITS ####################
        ## .npy binary file save
        output_path_disparity = youtube_dir + '/' + \
                                targets['img_1_path'][i].split('/')[-1][:-4] + '.npy'
        # print(output_path_disparity)
        disparity = np.tile(np.expand_dims(disparity, axis=-1), (1, 1, 3))
        np.save(output_path_disparity, disparity)
        ################# EDIT ENDS ##################

        ### Output Image has Comparison between original and depth map
        # saved_imgs = np.concatenate((saved_img, disparity), axis=1)
        # saved_imgs = (saved_imgs*255).astype(np.uint8)


        ################### EDITS ####################
        ### Output Image only has Depth Map
        # saved_imgs = (disparity * 255).astype(np.uint8)

        ### Output Image only has original image
        saved_imgs = saved_img
        saved_imgs = (saved_imgs * 255).astype(np.uint8)
        ################# EDIT ENDS ##################

        imsave(output_path, saved_imgs)
