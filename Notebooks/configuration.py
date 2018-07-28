class HierarchicalConfig:
    
    def __init__(self):
        self.config_dict = self.__build_conf_dict()
        self.config_dict['MODEL_MEANS'] = self.__load_means()
    
    def __build_conf_dict(self):
        return {
            'TEST_IMG_DIR': '/home/ubuntu/Data/Skin/Test/',
            'BATCH_SIZE': 16,
            'NV_IMG_DIMS': (168, 224),
            'OTHER_IMG_DIMS': (225, 300),
            'CACHE_DIR': '/home/ubuntu/Data/Skin/tmp',
            'CLASSES': ['MEL', 'NV', 'BCC', 'AKIEC', 'BKL', 'DF', 'VASC'],
            'MODEL_NAMES': {
                'NV_NON_NV': 'nv_non_nv_inceptionv3_512_custom_weight_init_full_train-ve1.h5',
                'DF_VASC_OTHERS': 'df_vasc_others_inceptionv3_512_full_train.h5',
                'BCC_OTHERS': 'bcc_others_inceptionv3_512_full_trainbias-pos25.h5',
                'AKIEC_OTHERS': 'akiec_non_akiec_inceptionv3_512_1.h5',
                'MEL_BKL': 'bkl_mel_inceptionv3_512_full_train.h5'
            },
            'MODEL_MEAN_PATHS': {
                'NV_NON_NV': '/home/ubuntu/Data/Skin/nv_non_nv/mean_image_nv_non_nv.npz',
                'DF_VASC_OTHERS': '/home/ubuntu/Data/Skin/df_vasc_others/mean_image_df_vasc_others.npz',
                'BCC_OTHERS': '/home/ubuntu/Data/Skin/bcc_others/mean_image_bcc_others.npz',
                'AKIEC_OTHERS': '/home/ubuntu/Data/Skin/akiec_others/mean_image_akiec_others.npz',
                'MEL_BKL': '/home/ubuntu/Data/Skin/mel_bkl/mean_image_mel_bkl.npz'
            },
            'MODEL_TAGS': {
                'NV_NON_NV': ['NON_NV', 'NV'],
                'DF_VASC_OTHERS': ['DF', 'VASC', 'OTHERS'],
                'BCC_OTHERS': ['NON_BCC', 'BCC'],
                'AKIEC_OTHERS': ['NON_AKIEC', 'AKIEC'],
                'MEL_BKL': ['BKL', 'MEL']
            },
            'PICKLE_FILES': {
                'NV_NON_NV': 'nv_predictions.pickle',
                'DF_VASC_OTHERS': 'df_vasc_predictions.pickle',
                'BCC_OTHERS': 'bcc_predictions.pickle',
                'AKIEC_OTHERS': 'akiec_predictions.pickle',
                'MEL_BKL': 'mel_bkl_predictions.pickle'
            }
        }
    
    def __load_means(self):
        import numpy as np
        from PIL import Image
        
        mean_images = dict()
        
        for key, val in self.config_dict['MODEL_MEAN_PATHS'].items():
            m = np.load(val)['image'].astype(np.uint8)
            if key == 'NV_NON_NV':
                im = Image.fromarray(m).resize((224, 168))
            else:
                im = Image.fromarray(m).resize((300, 225))
            
            mean_images[key] = np.asarray(im)
            
        return mean_images
        