"""Automatically generated by binding_generator.py.

MuJoCo header version: 232
"""

# pylint: disable=bad-continuation
# pylint: disable=line-too-long

array_sizes = (
{'mjdata': {'D_colind': ('nD',),
            'D_rowadr': ('nv',),
            'D_rownnz': ('nv',),
            'act': ('na',),
            'act_dot': ('na',),
            'actuator_force': ('nu',),
            'actuator_length': ('nu',),
            'actuator_moment': ('nu', 'nv'),
            'actuator_velocity': ('nu',),
            'cacc': ('nbody', 6),
            'cam_xmat': ('ncam', 9),
            'cam_xpos': ('ncam', 3),
            'cdof': ('nv', 6),
            'cdof_dot': ('nv', 6),
            'cfrc_ext': ('nbody', 6),
            'cfrc_int': ('nbody', 6),
            'cinert': ('nbody', 10),
            'crb': ('nbody', 10),
            'ctrl': ('nu',),
            'cvel': ('nbody', 6),
            'geom_xmat': ('ngeom', 9),
            'geom_xpos': ('ngeom', 3),
            'light_xdir': ('nlight', 3),
            'light_xpos': ('nlight', 3),
            'mocap_pos': ('nmocap', 3),
            'mocap_quat': ('nmocap', 4),
            'plugin': ('nplugin',),
            'plugin_data': ('nplugin',),
            'plugin_state': ('npluginstate',),
            'qDeriv': ('nD',),
            'qH': ('nM',),
            'qHDiagInv': ('nv',),
            'qLD': ('nM',),
            'qLDiagInv': ('nv',),
            'qLDiagSqrtInv': ('nv',),
            'qLU': ('nD',),
            'qM': ('nM',),
            'qacc': ('nv',),
            'qacc_smooth': ('nv',),
            'qacc_warmstart': ('nv',),
            'qfrc_actuator': ('nv',),
            'qfrc_applied': ('nv',),
            'qfrc_bias': ('nv',),
            'qfrc_constraint': ('nv',),
            'qfrc_inverse': ('nv',),
            'qfrc_passive': ('nv',),
            'qfrc_smooth': ('nv',),
            'qpos': ('nq',),
            'qvel': ('nv',),
            'sensordata': ('nsensordata',),
            'site_xmat': ('nsite', 9),
            'site_xpos': ('nsite', 3),
            'subtree_angmom': ('nbody', 3),
            'subtree_com': ('nbody', 3),
            'subtree_linvel': ('nbody', 3),
            'ten_J': ('ntendon', 'nv'),
            'ten_J_colind': ('ntendon', 'nv'),
            'ten_J_rowadr': ('ntendon',),
            'ten_J_rownnz': ('ntendon',),
            'ten_length': ('ntendon',),
            'ten_velocity': ('ntendon',),
            'ten_wrapadr': ('ntendon',),
            'ten_wrapnum': ('ntendon',),
            'userdata': ('nuserdata',),
            'wrap_obj': ('nwrap', 2),
            'wrap_xpos': ('nwrap', 6),
            'xanchor': ('njnt', 3),
            'xaxis': ('njnt', 3),
            'xfrc_applied': ('nbody', 6),
            'ximat': ('nbody', 9),
            'xipos': ('nbody', 3),
            'xmat': ('nbody', 9),
            'xpos': ('nbody', 3),
            'xquat': ('nbody', 4)},
 'mjmodel': {'actuator_acc0': ('nu',),
             'actuator_actadr': ('nu',),
             'actuator_actlimited': ('nu',),
             'actuator_actnum': ('nu',),
             'actuator_actrange': ('nu', 2),
             'actuator_biasprm': ('nu', 10),
             'actuator_biastype': ('nu',),
             'actuator_cranklength': ('nu',),
             'actuator_ctrllimited': ('nu',),
             'actuator_ctrlrange': ('nu', 2),
             'actuator_dynprm': ('nu', 10),
             'actuator_dyntype': ('nu',),
             'actuator_forcelimited': ('nu',),
             'actuator_forcerange': ('nu', 2),
             'actuator_gainprm': ('nu', 10),
             'actuator_gaintype': ('nu',),
             'actuator_gear': ('nu', 6),
             'actuator_group': ('nu',),
             'actuator_length0': ('nu',),
             'actuator_lengthrange': ('nu', 2),
             'actuator_plugin': ('nu',),
             'actuator_trnid': ('nu', 2),
             'actuator_trntype': ('nu',),
             'actuator_user': ('nu', 'nuser_actuator'),
             'body_dofadr': ('nbody',),
             'body_dofnum': ('nbody',),
             'body_geomadr': ('nbody',),
             'body_geomnum': ('nbody',),
             'body_gravcomp': ('nbody',),
             'body_inertia': ('nbody', 3),
             'body_invweight0': ('nbody', 2),
             'body_ipos': ('nbody', 3),
             'body_iquat': ('nbody', 4),
             'body_jntadr': ('nbody',),
             'body_jntnum': ('nbody',),
             'body_mass': ('nbody',),
             'body_mocapid': ('nbody',),
             'body_parentid': ('nbody',),
             'body_plugin': ('nbody',),
             'body_pos': ('nbody', 3),
             'body_quat': ('nbody', 4),
             'body_rootid': ('nbody',),
             'body_sameframe': ('nbody',),
             'body_simple': ('nbody',),
             'body_subtreemass': ('nbody',),
             'body_user': ('nbody', 'nuser_body'),
             'body_weldid': ('nbody',),
             'cam_bodyid': ('ncam',),
             'cam_fovy': ('ncam',),
             'cam_ipd': ('ncam',),
             'cam_mat0': ('ncam', 9),
             'cam_mode': ('ncam',),
             'cam_pos': ('ncam', 3),
             'cam_pos0': ('ncam', 3),
             'cam_poscom0': ('ncam', 3),
             'cam_quat': ('ncam', 4),
             'cam_targetbodyid': ('ncam',),
             'cam_user': ('ncam', 'nuser_cam'),
             'dof_M0': ('nv',),
             'dof_Madr': ('nv',),
             'dof_armature': ('nv',),
             'dof_bodyid': ('nv',),
             'dof_damping': ('nv',),
             'dof_frictionloss': ('nv',),
             'dof_invweight0': ('nv',),
             'dof_jntid': ('nv',),
             'dof_parentid': ('nv',),
             'dof_simplenum': ('nv',),
             'dof_solimp': ('nv', 5),
             'dof_solref': ('nv', 2),
             'eq_active': ('neq',),
             'eq_data': ('neq', 11),
             'eq_obj1id': ('neq',),
             'eq_obj2id': ('neq',),
             'eq_solimp': ('neq', 5),
             'eq_solref': ('neq', 2),
             'eq_type': ('neq',),
             'exclude_signature': ('nexclude',),
             'geom_bodyid': ('ngeom',),
             'geom_conaffinity': ('ngeom',),
             'geom_condim': ('ngeom',),
             'geom_contype': ('ngeom',),
             'geom_dataid': ('ngeom',),
             'geom_fluid': ('ngeom', 12),
             'geom_friction': ('ngeom', 3),
             'geom_gap': ('ngeom',),
             'geom_group': ('ngeom',),
             'geom_margin': ('ngeom',),
             'geom_matid': ('ngeom',),
             'geom_pos': ('ngeom', 3),
             'geom_priority': ('ngeom',),
             'geom_quat': ('ngeom', 4),
             'geom_rbound': ('ngeom',),
             'geom_rgba': ('ngeom', 4),
             'geom_sameframe': ('ngeom',),
             'geom_size': ('ngeom', 3),
             'geom_solimp': ('ngeom', 5),
             'geom_solmix': ('ngeom',),
             'geom_solref': ('ngeom', 2),
             'geom_type': ('ngeom',),
             'geom_user': ('ngeom', 'nuser_geom'),
             'hfield_adr': ('nhfield',),
             'hfield_data': ('nhfielddata',),
             'hfield_ncol': ('nhfield',),
             'hfield_nrow': ('nhfield',),
             'hfield_size': ('nhfield', 4),
             'jnt_axis': ('njnt', 3),
             'jnt_bodyid': ('njnt',),
             'jnt_dofadr': ('njnt',),
             'jnt_group': ('njnt',),
             'jnt_limited': ('njnt',),
             'jnt_margin': ('njnt',),
             'jnt_pos': ('njnt', 3),
             'jnt_qposadr': ('njnt',),
             'jnt_range': ('njnt', 2),
             'jnt_solimp': ('njnt', 5),
             'jnt_solref': ('njnt', 2),
             'jnt_stiffness': ('njnt',),
             'jnt_type': ('njnt',),
             'jnt_user': ('njnt', 'nuser_jnt'),
             'key_act': ('nkey', 'na'),
             'key_ctrl': ('nkey', 'nu'),
             'key_mpos': ('nkey', ('nmocap', 3)),
             'key_mquat': ('nkey', ('nmocap', 4)),
             'key_qpos': ('nkey', 'nq'),
             'key_qvel': ('nkey', 'nv'),
             'key_time': ('nkey',),
             'light_active': ('nlight',),
             'light_ambient': ('nlight', 3),
             'light_attenuation': ('nlight', 3),
             'light_bodyid': ('nlight',),
             'light_castshadow': ('nlight',),
             'light_cutoff': ('nlight',),
             'light_diffuse': ('nlight', 3),
             'light_dir': ('nlight', 3),
             'light_dir0': ('nlight', 3),
             'light_directional': ('nlight',),
             'light_exponent': ('nlight',),
             'light_mode': ('nlight',),
             'light_pos': ('nlight', 3),
             'light_pos0': ('nlight', 3),
             'light_poscom0': ('nlight', 3),
             'light_specular': ('nlight', 3),
             'light_targetbodyid': ('nlight',),
             'mat_emission': ('nmat',),
             'mat_reflectance': ('nmat',),
             'mat_rgba': ('nmat', 4),
             'mat_shininess': ('nmat',),
             'mat_specular': ('nmat',),
             'mat_texid': ('nmat',),
             'mat_texrepeat': ('nmat', 2),
             'mat_texuniform': ('nmat',),
             'mesh_face': ('nmeshface', 3),
             'mesh_faceadr': ('nmesh',),
             'mesh_facenum': ('nmesh',),
             'mesh_graph': ('nmeshgraph',),
             'mesh_graphadr': ('nmesh',),
             'mesh_normal': ('nmeshvert', 3),
             'mesh_texcoord': ('nmeshtexvert', 2),
             'mesh_texcoordadr': ('nmesh',),
             'mesh_vert': ('nmeshvert', 3),
             'mesh_vertadr': ('nmesh',),
             'mesh_vertnum': ('nmesh',),
             'name_actuatoradr': ('nu',),
             'name_bodyadr': ('nbody',),
             'name_camadr': ('ncam',),
             'name_eqadr': ('neq',),
             'name_excludeadr': ('nexclude',),
             'name_geomadr': ('ngeom',),
             'name_hfieldadr': ('nhfield',),
             'name_jntadr': ('njnt',),
             'name_keyadr': ('nkey',),
             'name_lightadr': ('nlight',),
             'name_matadr': ('nmat',),
             'name_meshadr': ('nmesh',),
             'name_numericadr': ('nnumeric',),
             'name_pairadr': ('npair',),
             'name_pluginadr': ('nplugin',),
             'name_sensoradr': ('nsensor',),
             'name_siteadr': ('nsite',),
             'name_skinadr': ('nskin',),
             'name_tendonadr': ('ntendon',),
             'name_texadr': ('ntex',),
             'name_textadr': ('ntext',),
             'name_tupleadr': ('ntuple',),
             'names': ('nnames',),
             'names_map': ('nnames_map',),
             'numeric_adr': ('nnumeric',),
             'numeric_data': ('nnumericdata',),
             'numeric_size': ('nnumeric',),
             'pair_dim': ('npair',),
             'pair_friction': ('npair', 5),
             'pair_gap': ('npair',),
             'pair_geom1': ('npair',),
             'pair_geom2': ('npair',),
             'pair_margin': ('npair',),
             'pair_signature': ('npair',),
             'pair_solimp': ('npair', 5),
             'pair_solref': ('npair', 2),
             'plugin': ('nplugin',),
             'plugin_attr': ('npluginattr',),
             'plugin_attradr': ('nplugin',),
             'plugin_stateadr': ('nplugin',),
             'plugin_statenum': ('nplugin',),
             'qpos0': ('nq',),
             'qpos_spring': ('nq',),
             'sensor_adr': ('nsensor',),
             'sensor_cutoff': ('nsensor',),
             'sensor_datatype': ('nsensor',),
             'sensor_dim': ('nsensor',),
             'sensor_needstage': ('nsensor',),
             'sensor_noise': ('nsensor',),
             'sensor_objid': ('nsensor',),
             'sensor_objtype': ('nsensor',),
             'sensor_plugin': ('nsensor',),
             'sensor_refid': ('nsensor',),
             'sensor_reftype': ('nsensor',),
             'sensor_type': ('nsensor',),
             'sensor_user': ('nsensor', 'nuser_sensor'),
             'site_bodyid': ('nsite',),
             'site_group': ('nsite',),
             'site_matid': ('nsite',),
             'site_pos': ('nsite', 3),
             'site_quat': ('nsite', 4),
             'site_rgba': ('nsite', 4),
             'site_sameframe': ('nsite',),
             'site_size': ('nsite', 3),
             'site_type': ('nsite',),
             'site_user': ('nsite', 'nuser_site'),
             'skin_boneadr': ('nskin',),
             'skin_bonebindpos': ('nskinbone', 3),
             'skin_bonebindquat': ('nskinbone', 4),
             'skin_bonebodyid': ('nskinbone',),
             'skin_bonenum': ('nskin',),
             'skin_bonevertadr': ('nskinbone',),
             'skin_bonevertid': ('nskinbonevert',),
             'skin_bonevertnum': ('nskinbone',),
             'skin_bonevertweight': ('nskinbonevert',),
             'skin_face': ('nskinface', 3),
             'skin_faceadr': ('nskin',),
             'skin_facenum': ('nskin',),
             'skin_group': ('nskin',),
             'skin_inflate': ('nskin',),
             'skin_matid': ('nskin',),
             'skin_rgba': ('nskin', 4),
             'skin_texcoord': ('nskintexvert', 2),
             'skin_texcoordadr': ('nskin',),
             'skin_vert': ('nskinvert', 3),
             'skin_vertadr': ('nskin',),
             'skin_vertnum': ('nskin',),
             'tendon_adr': ('ntendon',),
             'tendon_damping': ('ntendon',),
             'tendon_frictionloss': ('ntendon',),
             'tendon_group': ('ntendon',),
             'tendon_invweight0': ('ntendon',),
             'tendon_length0': ('ntendon',),
             'tendon_lengthspring': ('ntendon', 2),
             'tendon_limited': ('ntendon',),
             'tendon_margin': ('ntendon',),
             'tendon_matid': ('ntendon',),
             'tendon_num': ('ntendon',),
             'tendon_range': ('ntendon', 2),
             'tendon_rgba': ('ntendon', 4),
             'tendon_solimp_fri': ('ntendon', 5),
             'tendon_solimp_lim': ('ntendon', 5),
             'tendon_solref_fri': ('ntendon', 2),
             'tendon_solref_lim': ('ntendon', 2),
             'tendon_stiffness': ('ntendon',),
             'tendon_user': ('ntendon', 'nuser_tendon'),
             'tendon_width': ('ntendon',),
             'tex_adr': ('ntex',),
             'tex_height': ('ntex',),
             'tex_rgb': ('ntexdata',),
             'tex_type': ('ntex',),
             'tex_width': ('ntex',),
             'text_adr': ('ntext',),
             'text_data': ('ntextdata',),
             'text_size': ('ntext',),
             'tuple_adr': ('ntuple',),
             'tuple_objid': ('ntupledata',),
             'tuple_objprm': ('ntupledata',),
             'tuple_objtype': ('ntupledata',),
             'tuple_size': ('ntuple',),
             'wrap_objid': ('nwrap',),
             'wrap_prm': ('nwrap',),
             'wrap_type': ('nwrap',)}}
)
# ----------------------------End of generated code----------------------------
