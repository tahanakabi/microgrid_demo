from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField
from wtforms.validators import Optional, NumberRange



class ParamForm(FlaskForm):
    # parameters_list = ["iterations",
    #                    "num_tcls"
    #                    "tcl_power",
    #                    "tcl_price",
    #                    "num_loads",
    #                    "base_load",
    #                    "normal_price",
    #                    "temperatures",
    #                    "price_tiers",
    #                    "day0",
    #                    "dayn",
    #                    "power_cost",
    #                    "down_reg",
    #                    "up_reg",
    #                    "imp_fees",
    #                    "exp_fees",
    #                    "battery_capacity",
    #                    "max_discharge",
    #                    "max_charge"]
    # iterations = IntegerField("Number of timesteps",validators=[Optional()])
    num_tcls = IntegerField("Number of TCLs",validators=[Optional()], render_kw={'placeholder': 'Default:100'})
    tcl_power = FloatField("TCL average power (kW)",validators=[Optional()], render_kw={'placeholder':'Default: 1.5 kW'})
    tcl_price = FloatField("TCLs price (cents)",validators=[Optional()], render_kw={'placeholder': 'Default: 3.2 euro cents'})
    num_loads = IntegerField("Number of loads",validators=[Optional()], render_kw={'placeholder': 'Default: 150'})
    # base_load = FloatField("Typical load",validators=[Optional()])
    normal_price = FloatField("Normal retail price (cents)",validators=[Optional()], render_kw={'placeholder':'Default: 5.48 euro cents'})
    # temperatures = FloatField("Temperatures",validators=[Optional()])

    day0 = IntegerField("Day 0",validators=[Optional(), NumberRange(min=0, max=100, message="Please choose between 0 and 100")], render_kw={'placeholder':'Between 0 and 100. 0 = 1-1-2018'} )
    # dayn = IntegerField("Day N",validators=[Optional()])
    power_cost = FloatField("Power cost per kWh (cents)",validators=[Optional()],render_kw={'placeholder':'Default: 3.2 euro cents'} )
    # down_reg = FloatField("Down regulation prices",validators=[Optional()])
    # up_reg = FloatField("Up regulation prices",validators=[Optional()])
    imp_fees = FloatField("Power Transmission fees (import) ",validators=[Optional()], render_kw={'placeholder':'Default: 0.97 euro cents'})
    exp_fees = FloatField("Power Transmission fees (export) ",validators=[Optional()], render_kw={'placeholder':'Default: 0.09 euro cents'})
    battery_capacity = FloatField("Battery Capacity kWh",validators=[Optional()], render_kw={'placeholder': 'Default: 500 kWh'})
    max_discharge = FloatField("Discharge limit per hour",validators=[Optional()], render_kw={'placeholder': 'Default: 250 kWh'})
    max_charge = FloatField("Charge limit per hour",validators=[Optional()], render_kw={'placeholder':'Default: 250 kWh'})
    submit = SubmitField('Submit')
    # parameters_dict={}
    # for param in parameters_list:
    #     parameters_dict[param]= FloatField(param)

class NextDayForm(FlaskForm):
    next_day = SubmitField("Next Day")
    previous_day = SubmitField("Previous Day")