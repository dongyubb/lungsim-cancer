import os
from aether.diagnostics import set_diagnostics_on
from aether.indices import ventilation_indices, get_ne_radius
from aether.geometry import define_node_geometry, define_1d_elements, define_rad_from_file, append_units, get_terminal_density_from_file,set_volume_fromrv,set_constriction_from_file,define_rad_from_geom
from aether.ventilation import evaluate_vent
from aether.exports import export_1d_elem_geometry, export_node_geometry, export_elem_field, export_1d_elem_field, export_terminal_solution
from pulmonary.utils.io_files import get_default_output_path, get_default_geometry_path
from pulmonary.utils.bin_analysis import export_bin_results
from pulmonary.utils.solvers import solve_volume_from_cc


def main():
    set_diagnostics_on(False)
    patientid = 'lung005'
    protocal = 'baseline_cropped/GTV'

    density_tag = raw_input('Do you want to read density file? [yes/no]')
    constriction_tag = raw_input('Do you want to constrict the airways? [yes/no]')
    densitytag = False
    constrictiontag = False
    if density_tag.lower() == "yes":
        densitytag = True
    else:
        densitytag = False
    if constriction_tag.lower() == "yes":
        constrictiontag = True
    else:
        constrictiontag = False

    # Read settings
    ventilation_indices()

    define_node_geometry(get_default_geometry_path('AirwayTree_VF.ipnode', patientid, protocal))
    define_1d_elements(get_default_geometry_path('AirwayTree_VF.ipelem', patientid, protocal))
    #define_rad_from_geom('horsfield', 1.16, 'inlet', 6.7)
    define_rad_from_file(get_default_geometry_path('AirwayTree_VF.ipfiel', patientid, protocal))
    append_units()
    if densitytag == True:
    #read density file
        cc_dir = get_default_output_path('unit_cc.txt',patientid,protocal)
        get_terminal_density_from_file(
             get_default_geometry_path('AirwayTree_VF_node_with_density_GTV.txt', patientid, protocal),cc_dir)
        # v_dir = solve_volume_from_cc(cc_dir)
        # set_volume_fromrv(v_dir)
    if constrictiontag == True:
        constriction_dir = get_default_geometry_path('ElemToClose.txt',patientid,protocal)
        set_constriction_from_file(constriction_dir)

    # Set the working directory to the this files directory and then reset after running simulation.
    file_location = os.path.dirname(os.path.abspath(__file__))
    cur_dir = os.getcwd()
    os.chdir(file_location)
    #print(file_location)

    # Run simulation.
    evaluate_vent()

    # Set the working directory back to it's original location.
    os.chdir(cur_dir)

    # Output results
    # Export airway nodes and elements
    group_name = 'vent_model'
    export_1d_elem_geometry(get_default_output_path('AirwayTree_VF.exelem', patientid, protocal), group_name)
    export_node_geometry(get_default_output_path('AirwayTree_VF.exnode', patientid, protocal), group_name)

    # Export flow element
    field_name = 'flow'
    export_elem_field(get_default_output_path('ventilation_fields.exelem', patientid, protocal), group_name, field_name)

    # Export element field for radius
    ne_radius = get_ne_radius()
    field_name = 'radius'
    export_1d_elem_field(ne_radius, get_default_output_path('ventilation_radius_field.exelem', patientid, protocal), group_name, field_name)

    # Export terminal solution
    export_terminal_solution(get_default_output_path('terminal.exnode', patientid, protocal), group_name)

    # Export bin results
    export_bin_results(get_default_output_path('bin_results.txt', patientid, protocal), 20)



if __name__ == '__main__':
    main()

