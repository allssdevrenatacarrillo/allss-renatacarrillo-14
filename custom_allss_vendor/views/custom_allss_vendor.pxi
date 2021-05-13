<?xml version="1.0" encoding="utf-8"?>
<data>
    <record id="custom_allss_vendor" model="ir.ui.view">
        <field name="name">Vendor</field>
        <field name="model">project.task</field>
        <field name="inherit_id" ref="project.view_task_form2"/>
        <field name="arch" type="xml"> 

        <xpath expr="//group[2]" position="after">
            <h1>TEEEEEEESTE</h1>
            <field name="user_id" class="o_task_user_field" domain="[('share', '=', False)]" can_create="true" can_write="true" modifiers="{}" id="user_id"/>
        </xpath>
    </record>
</data>
