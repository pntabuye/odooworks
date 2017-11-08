# -*- coding: utf-8 -*-

from odoo import (
    models,
    fields,
    api
)


class MRArtist(models.Model):
    _name = 'musicregister.artist'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')


class MRAlbum(models.Model):
    """
    An album available for distribution is composed of on or more songs.
    When creating an album available songs are made available.
    """
    _name = 'musicregister.album'
    _description = 'musicregister album'
    _order = 'date desc'

    artist = fields.Char('Artist', required=True)
    title = fields.Char('Title', required=True)
    date = fields.Date('Date', required=True, readonly=False,
                       default=fields.Date.context_today)
    album_entry_ids = fields.One2many(
         'musicregister.album.entry',
         'album_id',
         'Songs',
         readonly=False,
         copy=True
    )


class MRAlbumEntry(models.Model):
    _name = 'musicregister.album.entry'
    _description = 'musicregister album entry'

    name = fields.Char(related='song_id.name', string='Song Title',
                       readonly=False)
    album_id = fields.Many2one('musicregister.album', 'Album',
                               ondelete='cascade', required=True,
                               readonly=True)
    title = fields.Char(related='album_id.title',
                        string='Album Title',
                        readonly=True)
    artist = fields.Char(related='album_id.artist',
                         string='Artist',
                         readonly=True)
    song_id = fields.Many2one('musicregister.song', 'Song', required=True)
    genre_id = fields.Many2one('musicregister.song.genre', string='Song Genre',
                               related='song_id.genre_id',
                               readonly=False, store=True)
    extras = fields.Text('Extras')


class MRSong(models.Model):
    """ Song available for compilation. """
    _name = 'musicregister.song'
    _description = 'musicregister song'

    name = fields.Char('Title', required=True)
    genre_id = fields.Many2one('musicregister.song.genre',
                               'Genre',
                               required=True)
    description = fields.Text('Description')


class MRSongGenre(models.Model):
    """ Music genres such as Rap, R&B , Afrobeat, Gakondo, ... """
    _name = 'musicregister.song.genre'
    _description = 'musicregister song genre'

    name = fields.Char('Genre', required=True)
