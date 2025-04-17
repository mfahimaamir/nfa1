#https://www.color-hex.com/
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode, AgGridTheme
import pandas as pd

# Sample data
df = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet", "Computer", "Table", "Train"],
    "stock": [45, 8, 15,55, 8, 5],
    "buy1": [445, 44, 45,45, 144, 5],
    "status": ["In Stock", "Low", "Low", "Low", "Low", "Low"]
})

# Custom cell styling based on stock levels
cellStyle = JsCode("""
function(params) {
    if (params.column.colId === 'stock') {
        if (params.value > 10) {
            return {
                'backgroundColor': '#ffebee',
                'color': '#c62828',
                'fontWeight': 'bold',
                'font-size': '24px'
                
            };
        } else if (params.value < 10) {
            return {
                'backgroundColor': '#fff3e0',
                'color': '#ef6c00'
            };
        }
    }
    

    if (params.column.colId === 'buy1') {
        if (params.value > 100) {
            return {
                'backgroundColor': '#f9b233',
                'color': '#c62828',
                'fontWeight': 'bold',
                'font-size': '14px'
            };
        } else if (params.value < 100) {
            return {
                'backgroundColor': '#fff3e0',
                'color': '#ef6c00'
            };
        }
    }

    
    return null;
    
}
""")

# Configure grid options
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_column("stock", cellStyle=cellStyle)
gb.configure_column("buy1", cellStyle=cellStyle)
gb.configure_column("status")
#gb.Style({'font-size': '24px'})
#gb.style = {'defaultColDef': {'fontSize': 24}} # Adjusts the font size to 14
#gridOptions = {'defaultColDef': {'fontSize': 24}} # Adjusts the font size to 14
#gridOptions = {'defaultColDef': {'fontSize': 14}} # Adjusts the font size to 14
#AgGrid(dataframe, gridOptions=gridOptions)

grid_options = gb.build()
#grid_options = {'defaultColDef': {'fontSize': 24}} # Adjusts the font size to 14
grid_return = AgGrid(
    df,style={'font-size': '24px'},
    gridOptions=grid_options,
    allow_unsafe_jscode=True
)




