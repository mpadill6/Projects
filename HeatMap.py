# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:22:18 2021

@author: mpadilla
"""
#%%
#Program to analyze images from UV LED camera and break down into R-G-B channel components.
#Each image is then sorted into a variety of folders depending on the entry number and combined with csv files with each pixel intensity
#Each image pixel table is converted to an array to form heatmaps to analyze pixel value trends and compare to false positive calls
#
#%%
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pa
parent_folder=r"\\kansas.us\qfs\QCI - R&D\Selective Access\R&D\Next Generation Immunoassay\Sniffles\Data\210406 UV LED Region Testing\Images\AI_Images"
cohorts=glob.glob(parent_folder+"/*")
for folder in cohorts:
    #folder=glob.glob(folder)
    plot_15_150_folder=folder+"\Plots(15-150)"
    plot_0_255_folder=folder+"\Plots(0-255)"
    plot_0_30_folder=folder+"\Plots(0-30)"
    csvfolder=folder+"\csv"
    Traces_folder=folder+"\Traces"
    for fileList in folder:
        fileList = glob.glob(folder+"/*.png")
    #%%
    
    for filename in fileList:
        image=cv2.imread(filename)
        image2=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        filename2=filename.split("\\")[-1]
        #format image_name[row, column, channel (0=r, 1=g, 2=b)]
        x=np.array(range(image2.shape[1]))
        y=np.array(range(image2.shape[0]))
        Red_data= np.zeros((len(y),len(x)))
        Green_data= np.zeros((len(y),len(x)))
        Blue_data= np.zeros((len(y),len(x)))
        #Generate data table for pixel intensities in red channel k=0 in image2[i,j,k]
        for i,yy in enumerate(y):
            for j, xx in enumerate(x):
                Red_data[i,j] = int(image2[i,j,0])
        Red_df=pa.DataFrame(Red_data)        
        Red_df.to_csv(csvfolder+'\Red_'+filename2[0:17]+'.csv')
        Red_Trace=Red_df.mean()
        Red_Trace.to_csv(Traces_folder+'\Line_Trace_Red_'+filename2[0:17]+'.csv')
        #Generate data table for pixel intensities in green channel k=1 in image2[i,j,k]
        for i,yy in enumerate(y):
            for j, xx in enumerate(x):
               Green_data[i,j] = image2[i,j,1]
        Green_df=pa.DataFrame(Green_data)
        Green_df.to_csv(csvfolder+'\Green_'+filename2[0:17]+'.csv')      
        #Generate data table for pixel intensities in blue channel k=2 in image2[i,j,k]
        for i,yy in enumerate(y):
            for j, xx in enumerate(x):
               Blue_data[i,j] = image2[i,j,2]  
        Blue_df=pa.DataFrame(Blue_data)
        Blue_df.to_csv(csvfolder+'\Blue_'+filename2[0:17]+'.csv')
       
        fig, ax=plt.subplots()
        img=ax.imshow(Red_data,cmap='nipy_spectral',vmin=0, vmax=255)
        cbar=fig.colorbar(mappable=img)  
        ax.set_xlabel('X Pixel Direction')
        ax.set_ylabel('Y Pixel Direction')
        ax.set_title("Heatmap_Red "+ filename2[0:17])
        plt.savefig(plot_0_255_folder+'\Red_'+filename2)
        plt.close(fig)
        
#        fig, ax=plt.subplots()
#        img=ax.imshow(Red_data,cmap='nipy_spectral',vmin=0, vmax=255)
#        cbar=fig.colorbar(mappable=img)  
#        ax.set_xlabel('X Pixel Direction')
#        ax.set_ylabel('Y Pixel Direction')
#        ax.set_title("Heatmap_Red "+ filename2[0:17])
#        plt.savefig(plot_0_30_folder+'\Red_'+filename2)
#        plt.close(fig) 
        
        fig, ax=plt.subplots()
        img=ax.imshow(Green_data,cmap='nipy_spectral', vmin=0, vmax=255)
        cbar=fig.colorbar(mappable=img)  
        ax.set_xlabel('X Pixel Direction')
        ax.set_ylabel('Y Pixel Direction')
        ax.set_title("Heatmap_Green "+ filename2[0:17])
        plt.savefig(plot_0_255_folder+'\Green_'+filename2)
        plt.close(fig)
    
#        fig, ax=plt.subplots()
#        img=ax.imshow(Green_data,cmap='nipy_spectral', vmin=0, vmax=255)
#        cbar=fig.colorbar(mappable=img)  
#        ax.set_xlabel('X Pixel Direction')
#        ax.set_ylabel('Y Pixel Direction')
#        ax.set_title("Heatmap_Green "+ filename2[0:17])
#        plt.savefig(plot_0_255_folder+'\Green_'+filename2)
#        plt.close(fig)  
        
        fig, ax=plt.subplots()
        img=ax.imshow(Blue_data,cmap='nipy_spectral',vmin=0, vmax=255)
        cbar=fig.colorbar(mappable=img)  
        ax.set_xlabel('X Pixel Direction')
        ax.set_ylabel('Y Pixel Direction')
        ax.set_title("Heatmap_Blue "+ filename2[0:17])
        plt.savefig(plot_0_255_folder+'\Blue_'+filename2)
        plt.close(fig)
    
#        fig, ax=plt.subplots()
#        img=ax.imshow(Blue_data,cmap='nipy_spectral',vmin=0, vmax=255)
#        cbar=fig.colorbar(mappable=img)  
#        ax.set_xlabel('X Pixel Direction')
#        ax.set_ylabel('Y Pixel Direction')
#        ax.set_title("Heatmap_Blue "+ filename2[0:17])
#        plt.savefig(plot_0_255_folder+'\Blue_'+filename2)
#        plt.close(fig)   
            

        
        plt.plot(x,Red_Trace) 
        plt.xlabel('X Pixel Direction')
        plt.ylabel('Average Y Value')
        plt.ylim(0,255)
        plt.title("Trace_Red_Channel "+ filename2[0:17])
        plt.grid()
        plt.savefig(Traces_folder+'\Red_'+filename2)
        plt.close('all')
