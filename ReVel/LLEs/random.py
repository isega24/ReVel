from ReVel.LLEs.LLE import LLE
import numpy as np
from sklearn.linear_model import Ridge

class RANDOM(LLE):
    '''
    RANDOM is a comparative Local Linear Explanation method. This method is not
    based on any algorithm. It is just a random method to compare with the behaviour of the other methods.
    
    '''
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def generate_neighbour(self,n_features:int)->np.ndarray:
        '''
        Generate a neighbour of the instance. The neighbour is actually
        not used in the method, but it is needed to be compatible with the
        LLE class.
        '''
        
        p = np.random.random()
        lista = np.array([i for i in range(n_features)])
        np.random.shuffle(lista)
        lista = lista[:p*len(lista)]
        
        return lista
    def kernel(self, V)->np.ndarray:
        '''
        The kernel is not used in the method, but it is needed to be compatible with the
        LLE class.
        
        Parameters
        ----------
        V : numpy.ndarray
            The feature vector of an instance.
            
        Returns
        -------
        The same feature vector. It is not used in the method.
        '''
        return V
    
    def regression(self, instance, model_forward, segments, examples)->Ridge:
        '''
        This regression method just returns a scikit-learn Ridge regression model with random weights generated by 
        np.random.rand().
        
        Parameters
        ----------
        instance : numpy.ndarray
            The feature vector of an instance. Used to calculate
            the dimensionality of the output.
        model_forward : numpy.ndarray
            The feature vector of the instance. Used to calculate
            the dimensionality of the output. 
        segments : numpy.ndarray
            The feature vector of the instance. Used to calculate
            the number of segments of the instance. 
        examples : numpy.ndarray
            The feature vector of the instance. Not used in the method.
        
        Returns
        -------
        sklearn.linear_model.Ridge
            The explanation proposed by the method.
        '''
        
        n_segments = len(np.unique(segments))
        out = model_forward(instance).detach().numpy()
        regressor_logits = Ridge(fit_intercept=True)
        
        regressor_logits.coef_ = np.random.rand(out.shape[1],n_segments)
        regressor_logits.intercept_ = np.random.rand(out.shape[1])
        return regressor_logits