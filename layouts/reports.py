import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from server import app
import pandas as pd
from datetime import datetime, timedelta
from plotly.subplots import make_subplots
import plotly.graph_objects as go


section_system_overview = html.Section(
    [
        html.H3('System Overview', className='col-12 mb-3'),
        html.Img(src=app.get_asset_url('images/Proxa_Monwabisi.jpg'),
                 className='col-9 mx-auto d-block')
    ],
    className='system-overview w-100'
)

section_date_range = html.Section(
    [
        html.H4('Data Range Selection', className='col-12 mb-3'),
        dbc.Row(
            [
                html.Div(
                    dcc.DatePickerSingle(
                        id='input_time_stamp_from',
                        date=(datetime.today() -
                              timedelta(days=1)).strftime('%Y-%m-%d'),
                        max_date_allowed=datetime.today(),
                        display_format='MM / DD'
                    ),
                    className='d-flex flex-column m-2'
                ),
                html.Div(
                    dcc.DatePickerSingle(
                        id='input_time_stamp_to',
                        date=datetime.today().strftime('%Y-%m-%d'),
                        max_date_allowed=datetime.today(),
                        display_format='MM / DD'
                    ),
                    className='d-flex flex-column m-2'
                ),
            ],
            className='mx-auto'
        ),
    ],
    className='input-data w-100'
)

DATAFILE_Path_Name = 'file.csv'
DATAFILE_Columns = ['t_stamp', 'FeedFlow', 'BackwashFlow', 'FeedPressure',
                    'FiltratePressure', 'TMPbar', 'FiltrateTurbidity', 'Permeability']
df = pd.read_csv(DATAFILE_Path_Name)
df['t_stamp'] = pd.to_datetime(df['t_stamp'])

section_input_data = html.Section(
    [
        html.H4('Input Data', className='col-12 mb-3'),
        dbc.Table.from_dataframe(
            df.head(), striped=True, bordered=True, hover=True)
    ],
    className='input-data w-100'
)

section_daily_performance_data = html.Section(
    [
        html.H4('Input Data', className='col-12 mb-3'),
        dbc.Table.from_dataframe(
            df.head(), striped=True, bordered=True, hover=True)
    ],
    className='input-data w-100'
)


section_daily_performance_data = html.Section(
    [
        html.H4('Daily Performance Data', className='col-12 mb-3'),
        dbc.Table.from_dataframe(
            df.head(), striped=True, bordered=True, hover=True)
    ],
    className='data-perfromance-data w-100'
)


def update_graph(start_date='2019-10-08', end_date='2019-10-17'):
    if start_date is not None:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%Y-%m-%d')

    if end_date is not None:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%Y-%m-%d')
    days_selected = (end_date - start_date).days

    df['DeltaPbar'] = df['TMPbar'].values
    df['Bed_Permeability'] = df['Permeability'].values
    df['Date'] = df['t_stamp'].dt.strftime('%Y-%m-%d')
    filtered_df = df[(df['t_stamp'] >= start_date_string) & (df['t_stamp'] <= end_date_string)].groupby(
        'Date').mean().reset_index()

    feed_flow_rate = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['FeedFlow'],
        name='Feed Flow',
        text='Feed Flow Rate (CMH)'
    )

    backwash_flow_rate = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['BackwashFlow'],
        name='Backwash Flow',
        text='Backwash Flow Rate (CMH)'
    )

    feed_pressure = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['FeedPressure'],
        name='Feed Pressure',
        text='Feed Pressure (bar)'
    )

    filtrate_pressure = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['FiltratePressure'],
        name='Filtrate Pressure',
        text='Filtrate Pressure (bar)'
    )

    dp_bar = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['DeltaPbar'],
        name='Bed Pressure Drop',
        text='Bed Pressure Drop (bar)'
    )

    permeability_bed = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['Bed_Permeability'],
        name='Permeability',
        text='Bed Permeability (LMH/bar)'
    )

    filtrate_turbidity = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['FiltrateTurbidity'],
        name='Filtrate Turbidity',
        text='Filtrate Turbidity (NTU)'
    )

    fig = make_subplots(
        rows=4,
        cols=1,
        shared_xaxes=True,
        subplot_titles=(  # Be sure to have same number of titles as number of graphs
            'Flow Rate (CMH)',
            'Pressures (bar)',
            'Permeability (LMH/bar)',
            'Turbidity (NTU)'
        ))

    fig.append_trace(feed_flow_rate, 1, 1)          # 0
    fig.append_trace(backwash_flow_rate, 1, 1)      # 1
    fig.append_trace(feed_pressure, 2, 1)           # 2
    fig.append_trace(filtrate_pressure, 2, 1)       # 3
    fig.append_trace(dp_bar, 2, 1)                  # 4
    fig.append_trace(permeability_bed, 3, 1)        # 5
    fig.append_trace(filtrate_turbidity, 4, 1)      # 6
    # fig.append_trace(bookings_ly, 3, 1)      # 7
    # fig.append_trace(bookings_yoy, 3, 1)     # 8
    # fig.append_trace(cpa_ty, 4, 1)           # 9
    # fig.append_trace(cpa_ly, 4, 1)           # 10
    # fig.append_trace(cpa_yoy, 4, 1)          # 11
    # fig.append_trace(cps_ty, 5, 1)           # 12
    # fig.append_trace(cps_ly, 5, 1)           # 13
    # fig.append_trace(cps_yoy, 5, 1)          # 14
    # fig.append_trace(cr_ty, 6, 1)            # 15
    # fig.append_trace(cr_ly, 6, 1)            # 16
    # fig.append_trace(cr_yoy, 6, 1)           # 17
    # integer index below is the index of the trace

    # yaxis indices below need to start from the number of total graphs + 1 since they are on right-side

    # overlaying and anchor axes correspond to the graph number

    fig['layout']['xaxis'].update(title='Date')

    fig['layout'].update(
        height=1000,
        width=750,
        showlegend=True,
        xaxis=dict(
            # tickmode='linear',
            # ticks='outside',
            # tick0=1,
            dtick=5,
            ticklen=8,
            tickwidth=2,
            tickcolor='#000',
            showgrid=True,
            zeroline=True,
            # showline=True,
            # mirror='ticks',
            gridcolor='#bdbdbd',
            gridwidth=2
        ),
    )

    updated_fig = fig
    return updated_fig


def get_layout():
    return dbc.Row(
        [
            section_system_overview,
            html.Hr(className='col-12'),
            section_date_range,
            html.Hr(className='col-12'),
            section_input_data,
            html.Hr(className='col-12'),
            section_daily_performance_data,
            dcc.Graph(figure=update_graph())
        ],
        className='reports-board'
    )
