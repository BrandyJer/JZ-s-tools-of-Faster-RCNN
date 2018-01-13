init:以16×16为基准，（8,16,32）为系数，生成面积为128×128,256×256,512×512，比例为1:2,1:1,2:1的9种anchor。

迭代次数改为25000
2017-12-19
修改锚点长宽比：0.5,1,2================>1.33,1.0,1.5
2017-12-20
修改锚尺度为1种：128*128,256*256,512*512===========>128*128
2017-12-29
修改锚尺度为2种：75*75, 122*122
长宽尺度比为2种：1：1, 2：1
具体修改：generat_anchor.py
======================================================================================================
2018-1-6
修改锚尺度为2种：55*55, 85*85
长宽尺度比为1种：1：1
具体修改：generat_anchor.py: 以5*5为基准，（11,17）为系数，生成面积为55×55,85×85，比例为1:1的两种anchor。
def generate_anchors(base_size=5, ratios=[1],
                     scales=[11, 17]):

有报错：Check failed: outer_num_ * inner_num_ == bottom[1]->count() (21546 vs. 7182) Number of labels must match number of predictions; e.g., if softmax axis == 1 and prediction shape is (N, C, H, W), label count (number of labels) must be N*H*W, with integer values in {0, 1, ..., C-1}.
因此注意：同时修改train.prototxt，text.prototxt文件：anchor=9的部分改为乘以anchor=2;
修改def generate_anchors(base_size=5, ratios=[1],
                     scales=np.array([11, 17])):
######JZ==>array([-25, -25, 29, 29]
######           [-40, -40, 44, 44])
======================================================================================================
修改anchor_target_layer.py
anchor_scales = layer_params.get('scales', (11, 17))
Check failed: 0 == bottom[0]->count() % explicit_count (0 vs. 504) bottom count (9576) must be divisible by the product of the specified dimensions (1134)
======================================================================================================
修改train.prototxt
layer'rpn_cls_prob_reshape':dim18=======>dim4
Traceback (most recent call last):
  File "./tools/train_net.py", line 116, in <module>
    max_iters=args.max_iters, previous_state=args.previous_state)
  File "/home/jz/py-faster-rcnn/tools/../lib/fast_rcnn/train.py", line 164, in train_net
    model_paths = sw.train_model(max_iters)
  File "/home/jz/py-faster-rcnn/tools/../lib/fast_rcnn/train.py", line 105, in train_model
    self.solver.step(1)
  File "/home/jz/py-faster-rcnn/tools/../lib/rpn/proposal_layer.py", line 122, in forward
    proposals = bbox_transform_inv(anchors, bbox_deltas)
  File "/home/jz/py-faster-rcnn/tools/../lib/fast_rcnn/bbox_transform.py", line 46, in bbox_transform_inv
    pred_ctr_x = dx * widths[:, np.newaxis] + ctr_x[:, np.newaxis]
ValueError: operands could not be broadcast together with shapes (3800,1) (5700,1) 
======================================================================================================
修改proposal_layer.py
anchor_scales = layer_params.get('scales', (11, 17))
==================================================================================================================
2018-1-10
修改pascal_voc.py中
# PASCAL specific config options
        self.config = {'cleanup'     : True,
                       'use_salt'    : True,
                       'use_diff'    : False,
                       'matlab_eval' : False,
                       'rpn_file'    : None,
                       'min_size'    : 2}
为(保存结果文件)
# PASCAL specific config options
        self.config = {'cleanup'     : False,
                       'use_salt'    : True,
                       'use_diff'    : False,
                       'matlab_eval' : False,
                       'rpn_file'    : None,
                       'min_size'    : 2}
=====================================================================================================
将上一项中的修改恢复default:cleanup:False
注释pascal_voc.py 328line
因此不删除template的detecte结果txt文件。
=====================================================================================================

