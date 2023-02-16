tournament_q = """query TournamentQuery($slug: String) {
                tournament(slug: $slug){
                    id
                    name
                    events {
                        id
                        name
                videogame {
                id
                }
                    }
                }
            }"""
