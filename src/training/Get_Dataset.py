class Get_Dataset( Dataset ):
    def __init__ (self) : #intial function define all member and  class variables 
        super(Get_Dataset , self).__init__()
        scale = 255
        path = './data/images'
        trainA = os.listdir(path + 'image')
        trainB = os.listdir(path + 'mask')
        self.len = min([len(image) , len(mask)])
        self.object = np.ones((self.len ,128,128 , 3 ))
        self.target = np.ones((self.len , 128 , 128 , 3))
        print("Loading Dataset...")
        for i in tqdm(range(self.len)) :
            self.object[i] = cv2.resize(cv2.imread(path + 'image/' + image[i]),  (128,128))
            self.target[i] = cv2.resize(cv2.imread(path + 'mask/' + mask[i]),  (128,128))
        self.object =  torch.from_numpy(((self.object/(scale/2))-1 ) ).transpose_(3 , 1).double()
        self.target = torch.from_numpy(((self.target/(scale / 2)) -1 )).transpose_(3 , 1).double()

    def __getitem__(self , index   ) : # function to return dataset size
        return self.object[index] ,  self.target[index]

    def __len__(self): #you must have this function
        return self.len