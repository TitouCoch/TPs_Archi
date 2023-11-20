# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x0e\n\x0c\x45mptyBooking\"\x1f\n\rBookingUserId\x12\x0e\n\x06userid\x18\x01 \x01(\t\"7\n\x0b\x42ookingData\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x18\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\t.DateData\"2\n\x13ShowtimesDataByDate\x12\x1b\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\t.DateData\"0\n\x08\x44\x61teData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x16\n\x06movies\x18\x02 \x03(\x0b\x32\x06.Movie\"B\n\x13ShowtimeByMovieData\x12\x15\n\x05movie\x18\x01 \x01(\x0b\x32\x06.Movie\x12\x14\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x05.Date\"3\n\x0f\x42ookingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x16\n\x05Movie\x12\r\n\x05movie\x18\x01 \x01(\t\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t2\xb2\x04\n\x07\x42ooking\x12\x34\n\x12GetBookingByUserID\x12\x0e.BookingUserId\x1a\x0c.BookingData\"\x00\x12\x32\n\x0fGetListBookings\x12\r.EmptyBooking\x1a\x0c.BookingData\"\x00\x30\x01\x12\x39\n\x10GetListShowtimes\x12\r.EmptyBooking\x1a\x14.ShowtimesDataByDate\"\x00\x12.\n\nAddBooking\x12\x0c.BookingData\x1a\x10.BookingResponse\"\x00\x12\x31\n\rUpdateBooking\x12\x0c.BookingData\x1a\x10.BookingResponse\"\x00\x12\x31\n\rDeleteBooking\x12\x0c.BookingData\x1a\x10.BookingResponse\"\x00\x12\x34\n\x12GetShowtimeByMovie\x12\x06.Movie\x1a\x14.ShowtimeByMovieData\"\x00\x12\'\n\x11GetShowtimeByDate\x12\x05.Date\x1a\t.DateData\"\x00\x12-\n\x0c\x41\x64\x64_Showtime\x12\t.DateData\x1a\x10.BookingResponse\"\x00\x12\x30\n\x0fUpdate_Showtime\x12\t.DateData\x1a\x10.BookingResponse\"\x00\x12,\n\x0f\x44\x65lete_Showtime\x12\x05.Date\x1a\x10.BookingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTYBOOKING']._serialized_start=17
  _globals['_EMPTYBOOKING']._serialized_end=31
  _globals['_BOOKINGUSERID']._serialized_start=33
  _globals['_BOOKINGUSERID']._serialized_end=64
  _globals['_BOOKINGDATA']._serialized_start=66
  _globals['_BOOKINGDATA']._serialized_end=121
  _globals['_SHOWTIMESDATABYDATE']._serialized_start=123
  _globals['_SHOWTIMESDATABYDATE']._serialized_end=173
  _globals['_DATEDATA']._serialized_start=175
  _globals['_DATEDATA']._serialized_end=223
  _globals['_SHOWTIMEBYMOVIEDATA']._serialized_start=225
  _globals['_SHOWTIMEBYMOVIEDATA']._serialized_end=291
  _globals['_BOOKINGRESPONSE']._serialized_start=293
  _globals['_BOOKINGRESPONSE']._serialized_end=344
  _globals['_MOVIE']._serialized_start=346
  _globals['_MOVIE']._serialized_end=368
  _globals['_DATE']._serialized_start=370
  _globals['_DATE']._serialized_end=390
  _globals['_BOOKING']._serialized_start=393
  _globals['_BOOKING']._serialized_end=955
# @@protoc_insertion_point(module_scope)
