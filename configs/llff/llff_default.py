_base_ = '../default.py'

basedir = '/data/liufengyi/Results/VoxGo_rewrite'

data = dict(
    dataset_type='llff',
    ndc=True,
    width=1008,
    height=756,
)

coarse_train = dict(
    N_iters=0,
)

fine_train = dict(
    N_iters=30000,
    N_rand=4096,
    weight_distortion=0.01,
    pg_scale=[2000,4000,6000,8000],
    ray_sampler='flatten',
    tv_before=1e9,
    tv_dense_before=10000,
    weight_tv_density=1e-5,
    weight_tv_k0=1e-6,
    weight_tv_hash=1e-5,
)

fine_model_and_render = dict(
    num_voxels=256**3,
    mpi_depth=128,
    rgbnet_dim=9,
    rgbnet_width=64,
    world_bound_scale=1,
    fast_color_thres=1e-3,
    
    hash_channel = 28,
    hidden_features = 128,
    hidden_layers = 1,
    out_features = 28,
    use_fine = True, 
    use_sh = True, 
    hash_type='DenseGrid',        #Add
    
)

