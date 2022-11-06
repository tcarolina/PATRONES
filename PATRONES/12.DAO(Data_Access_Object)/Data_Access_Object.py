def get_packs_for_anime_group():
    dao = DAO(db.session)
    aid = request.args.get("aid")
    group_name = request.args.get("group_name")
    file_packs = dao.get_packs_for_group_anime(aid, group_name)
    return jsonify(json_list=[e.serialize() for e in file_packs])
    