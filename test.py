import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import plotly
import plotly.express as px
import cufflinks as cf
cf.go_offline()

# Load the datasets
df = pd.read_csv('zomato.csv',encoding='latin1')

# Get the list of DataFrame columns
columns = df.columns.to_list()

# Select columns for x and y axes
sub_plot_type = ["Interactive Plots", "3D Plots", "Animation Plots"]
choice1 = st.sidebar.selectbox("Select Activities", sub_plot_type)

if choice1 == "Interactive Plots":
    plot_type = ["scatter", "bar", "pie", "sunburst", "treemap", "histogram", "box", "violin", "strip", "density heatmap"]
    choice = st.selectbox("Select Plot Type", plot_type)

    if choice == "scatter":
        # select column for scatter plot
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.scatter(df, x=x_col, y=y_col, color=color_col)
        st.plotly_chart(fig)

    elif choice == "bar":
        # bar plot with group
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.bar(df, x=x_col, y=y_col, color=color_col, barmode="group")
        st.plotly_chart(fig)

    elif choice == "pie":
        val_col = st.selectbox("Select value column", columns)
        name_col = st.selectbox("Select name column", columns)
        fig = px.pie(df, values=val_col, names=name_col, color_discrete_sequence=px.colors.sequential.Plotly3)
        st.plotly_chart(fig)

    elif choice == "sunburst":
        path_cols = st.multiselect("Select path columns", columns)
        val_col = st.selectbox("Select value column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.sunburst(df, path=path_cols, values=val_col, color=color_col)
        st.plotly_chart(fig)

    elif choice == "treemap":
        path_cols = st.multiselect("Select path columns", columns)
        val_col = st.selectbox("Select value column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.treemap(df, path=path_cols, values=val_col, color=color_col)
        st.plotly_chart(fig)

    elif choice == "histogram":
        x_col = st.selectbox("Select x-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.histogram(df, x=x_col, color=color_col, marginal="violin")
        st.plotly_chart(fig)

    elif choice == "box":
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.box(df, x=x_col, y=y_col, color=color_col)
        st.plotly_chart(fig)

    elif choice == "violin":
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.violin(df, y=y_col, x=x_col, color=color_col, box=True, points="all", hover_data=df.columns)
        st.plotly_chart(fig)

    elif choice == "strip":
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.strip(df, x=x_col, y=y_col, orientation="h", color=color_col)
        st.plotly_chart(fig)

    elif choice == "density heatmap":
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        fig = px.density_heatmap(df, x=x_col, y=y_col, marginal_x="rug", marginal_y="histogram", color_continuous_scale='Viridis')
        st.plotly_chart(fig)

elif choice1 == "3D Plots":
    plot_3d = ['scatter3d', 'line3d']
    plot_type2 = st.selectbox("Select 3D plot type", plot_3d)

    if plot_type2 == 'scatter3d':
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        z_col = st.selectbox("Select z-axis column", columns)
        color_col = st.selectbox("Select color column", columns)
        fig = px.scatter_3d(df, x=x_col, y=y_col, z=z_col, color=color_col, opacity=0.7)
        st.plotly_chart(fig)

    elif plot_type2 == 'line3d':
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        z_col = st.selectbox("Select z-axis column", columns)
        
        fig = px.line_3d(df, x=x_col, y=y_col, z=z_col)
        st.plotly_chart(fig)

elif choice1 == "Animation Plots":
    ani_plots=['Animation scatter', 'Animation bar']
    plot_type3=st.selectbox("Select animation plot type",ani_plots)
    if plot_type3 == 'Animation scatter':
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        ani_col = st.selectbox("Select animation frame column", columns)
        anig_col = st.selectbox("Select animation group column", columns)
        color_col = st.selectbox("Select color column", columns)
        si_col = st.selectbox("Select size column", columns)
        h_col = st.selectbox("Select hover name column", columns)
    
        fig = px.scatter(df, x=x_col, y=y_col, animation_frame=ani_col, animation_group=anig_col, size=si_col, color=color_col,
                         hover_name=h_col, log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])
    
        st.write(fig)
    
    
    elif plot_type3 == 'Animation bar':
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)
        ani_col = st.selectbox("Select animation frame column", columns)
        anig_col = st.selectbox("Select animation group column", columns)
        color_col = st.selectbox("Select color column", columns)
        
        fig = px.bar(df, x=x_col, y=y_col, color=color_col,
             animation_frame=ani_col, animation_group=anig_col, range_y=[0,4000000000])
        st.write(fig)
    

    
    
    
    
