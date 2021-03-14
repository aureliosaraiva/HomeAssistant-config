{% for state in states.sensor -%}
  {%- if 'battery' in state.entity_id -%}
  - entity: {{ state.entity_id }} {{ '\n' }}
  {%- endif -%}
{%- endfor %}

{% for state in states.binary_sensor -%}
  {%- if 'door' in state.entity_id and '_contact' in state.entity_id -%}
  {{ state.entity_id }} {{ '\n' }}
  {%- endif -%}
{%- endfor %}

    - type: entities
        title: Hall 2
        state_color: true
        entities:
          - switch.switch_wall_hall_2_l1
          - switch.switch_wall_hall_2_l2
          - switch.switch_wall_hall_2_l3
          - switch.switch_wall_hall_2_l4
    - type: entities
        title: Hall 1
        state_color: true
        entities:
          - switch.switch_wall_hall_1_garage
          - switch.switch_wall_1_light_l2
          - switch.switch_wall_hall_1_l3
          - switch.switch_wall_hall_1_l4
    - type: entities
        title: Cozinha
        state_color: true
        entities:
          - switch.switch_wall_kitchen_top
          - switch.switch_wall_kitchen_center
          - switch.switch_wall_kitchen_bottom
    - type: entities
        title: Sala (Jardim)
        state_color: true
        entities:
          - switch.switch_wall_garden_top
          - switch.switch_wall_garden_center
          - switch.switch_wall_garden_bottom
    - type: entities
        title: Laanderia
        state_color: true
        entities:
          - switch.switch_wall_laundry_top
          - switch.switch_wall_laundry_center
          - switch.switch_wall_laundry_bottom
    - type: entities
        title: Sala
        state_color: true
        entities:
          - switch.switch_wall_livingroom_top
          - switch.switch_wall_livingroom_center
          - switch.switch_wall_livingroom_bottom
    - type: entities
        title: Banheiro Suite
        state_color: true
        entities:
          - switch.switch_wall_bathroom_top
          - switch.switch_wall_bathroom_center
          - switch.switch_wall_bathroom_bottom
    - type: entities
        title: Hall 3
        state_color: true
        entities:
          - switch.switch_wall_hall_3_top
          - switch.switch_wall_hall_3_center
          - switch.switch_wall_hall_3_bottom
    - type: entities
        title: Laboratorio
        state_color: true
        entities:
          - switch.switch_wall_laboratory_top
          - switch.switch_wall_laboratory_center
          - switch.switch_wall_laboratory_bottom
    - type: entities
        title: Suite
        state_color: true
        entities:
          - switch.switch_wall_bedroom_top
          - switch.switch_wall_bedroom_center
          - switch.switch_wall_bedroom_bottom
    - type: entities
        title: Closet
        state_color: true
        entities:
          - switch.switch_wall_closet_top
          - switch.switch_wall_closet_center
          - switch.switch_wall_closet_bottom
