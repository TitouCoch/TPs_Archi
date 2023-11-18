# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBookingByUserID = channel.unary_unary(
                '/Booking/GetBookingByUserID',
                request_serializer=booking__pb2.BookingUserId.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetListBookings = channel.unary_stream(
                '/Booking/GetListBookings',
                request_serializer=booking__pb2.EmptyBooking.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetListShowtimes = channel.unary_unary(
                '/Booking/GetListShowtimes',
                request_serializer=booking__pb2.EmptyBooking.SerializeToString,
                response_deserializer=booking__pb2.ShowtimesDataByDate.FromString,
                )
        self.AddBooking = channel.unary_unary(
                '/Booking/AddBooking',
                request_serializer=booking__pb2.BookingData.SerializeToString,
                response_deserializer=booking__pb2.BookingResponse.FromString,
                )
        self.UpdateBooking = channel.unary_unary(
                '/Booking/UpdateBooking',
                request_serializer=booking__pb2.BookingData.SerializeToString,
                response_deserializer=booking__pb2.BookingResponse.FromString,
                )
        self.DeleteBooking = channel.unary_unary(
                '/Booking/DeleteBooking',
                request_serializer=booking__pb2.BookingUserId.SerializeToString,
                response_deserializer=booking__pb2.BookingResponse.FromString,
                )
        self.GetShowtimeByMovie = channel.unary_unary(
                '/Booking/GetShowtimeByMovie',
                request_serializer=booking__pb2.Movie.SerializeToString,
                response_deserializer=booking__pb2.ShowtimeByMovieData.FromString,
                )
        self.GetShowtimeByDate = channel.unary_unary(
                '/Booking/GetShowtimeByDate',
                request_serializer=booking__pb2.Date.SerializeToString,
                response_deserializer=booking__pb2.DateData.FromString,
                )
        self.Add_Showtime = channel.unary_unary(
                '/Booking/Add_Showtime',
                request_serializer=booking__pb2.DateData.SerializeToString,
                response_deserializer=booking__pb2.BookingResponse.FromString,
                )
        self.Update_Showtime = channel.unary_unary(
                '/Booking/Update_Showtime',
                request_serializer=booking__pb2.DateData.SerializeToString,
                response_deserializer=booking__pb2.BookingResponse.FromString,
                )
        self.Delete_Showtime = channel.unary_unary(
                '/Booking/Delete_Showtime',
                request_serializer=booking__pb2.Date.SerializeToString,
                response_deserializer=booking__pb2.BookingResponse.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBookingByUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListShowtimes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShowtimeByMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShowtimeByDate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Add_Showtime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update_Showtime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete_Showtime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBookingByUserID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookingByUserID,
                    request_deserializer=booking__pb2.BookingUserId.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetListBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListBookings,
                    request_deserializer=booking__pb2.EmptyBooking.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetListShowtimes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetListShowtimes,
                    request_deserializer=booking__pb2.EmptyBooking.FromString,
                    response_serializer=booking__pb2.ShowtimesDataByDate.SerializeToString,
            ),
            'AddBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBooking,
                    request_deserializer=booking__pb2.BookingData.FromString,
                    response_serializer=booking__pb2.BookingResponse.SerializeToString,
            ),
            'UpdateBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBooking,
                    request_deserializer=booking__pb2.BookingData.FromString,
                    response_serializer=booking__pb2.BookingResponse.SerializeToString,
            ),
            'DeleteBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBooking,
                    request_deserializer=booking__pb2.BookingUserId.FromString,
                    response_serializer=booking__pb2.BookingResponse.SerializeToString,
            ),
            'GetShowtimeByMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShowtimeByMovie,
                    request_deserializer=booking__pb2.Movie.FromString,
                    response_serializer=booking__pb2.ShowtimeByMovieData.SerializeToString,
            ),
            'GetShowtimeByDate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShowtimeByDate,
                    request_deserializer=booking__pb2.Date.FromString,
                    response_serializer=booking__pb2.DateData.SerializeToString,
            ),
            'Add_Showtime': grpc.unary_unary_rpc_method_handler(
                    servicer.Add_Showtime,
                    request_deserializer=booking__pb2.DateData.FromString,
                    response_serializer=booking__pb2.BookingResponse.SerializeToString,
            ),
            'Update_Showtime': grpc.unary_unary_rpc_method_handler(
                    servicer.Update_Showtime,
                    request_deserializer=booking__pb2.DateData.FromString,
                    response_serializer=booking__pb2.BookingResponse.SerializeToString,
            ),
            'Delete_Showtime': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete_Showtime,
                    request_deserializer=booking__pb2.Date.FromString,
                    response_serializer=booking__pb2.BookingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBookingByUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetBookingByUserID',
            booking__pb2.BookingUserId.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetListBookings',
            booking__pb2.EmptyBooking.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListShowtimes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetListShowtimes',
            booking__pb2.EmptyBooking.SerializeToString,
            booking__pb2.ShowtimesDataByDate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/AddBooking',
            booking__pb2.BookingData.SerializeToString,
            booking__pb2.BookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/UpdateBooking',
            booking__pb2.BookingData.SerializeToString,
            booking__pb2.BookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/DeleteBooking',
            booking__pb2.BookingUserId.SerializeToString,
            booking__pb2.BookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShowtimeByMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetShowtimeByMovie',
            booking__pb2.Movie.SerializeToString,
            booking__pb2.ShowtimeByMovieData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShowtimeByDate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetShowtimeByDate',
            booking__pb2.Date.SerializeToString,
            booking__pb2.DateData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Add_Showtime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/Add_Showtime',
            booking__pb2.DateData.SerializeToString,
            booking__pb2.BookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update_Showtime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/Update_Showtime',
            booking__pb2.DateData.SerializeToString,
            booking__pb2.BookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete_Showtime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/Delete_Showtime',
            booking__pb2.Date.SerializeToString,
            booking__pb2.BookingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
