sql_stmt = ('SELECT comic.page, comic.url, comic.title, comic.date,'
              ' count(*) n FROM chars'
              ' INNER JOIN comic ON comic.page == chars.page'
              ' LEFT JOIN alias ON character == alias.name'
              ' WHERE lower(CHARACTER) IN ({}) OR '
              ' lower(alias.name) in ({})'
              ' group by comic.page having n == {}'
              ' ORDER BY comic.page;')
