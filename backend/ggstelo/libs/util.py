def get_slug(slug):
    if type(slug) == str:
        return slug.replace(
            "user/", "")
    else:
        return "No Slug"

def get_sets(t_slug, e_slug):
  i = 1
  sets = []

  while (i > 0):
    results = smash.tournament_show_sets(t_slug, e_slug, i)
    sets.extend(results)

    if results == []:
      break
    i += 1

  return sets
