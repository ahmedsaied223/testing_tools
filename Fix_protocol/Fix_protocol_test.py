## Here's a Python script template for FIX protocol integration with trading systems support. This example uses the `quickfix` library, a popular FIX protocol implementation:

#!/usr/bin/env python3
import quickfix as fix
import quickfix44 as fix44
import logging
from datetime import datetime
import time
from time import sleepclass FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):



class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()
    
    
class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')


class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()
    
    
class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')

class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def send_cancel(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send OrderCancelRequest (F) message"""
        try:
            message = fix44.OrderCancelRequest()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.OrigClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Cancel sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send cancel: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Example: Send test cancel
        application.send_cancel(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')

# Configure logging
logging.basicConfig(level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')

class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

if __name__ == "__main__":
    main()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FIXEngine')

class FIXApplication(fix.Application):
    """Base FIX Application implementation for trading system integration"""

    def onCreate(self, sessionID):
        logger.info(f"Session created: {sessionID.toString()}")

    def onLogon(self, sessionID):
        logger.info(f"Successfully logged on: {sessionID.toString()}")

    def onLogout(self, sessionID):
        logger.info(f"Session logged out: {sessionID.toString()}")

    def toAdmin(self, message, sessionID):
        logger.debug(f"Sent admin message: {message.toString()}")

    def fromAdmin(self, message, sessionID):
        logger.debug(f"Received admin message: {message.toString()}")

    def toApp(self, message, sessionID):
        logger.debug(f"Sending application message: {message.toString()}")

    def fromApp(self, message, sessionID):
        self.onMessage(message, sessionID)

    def onMessage(self, message, sessionID):
        """Handle incoming application messages"""
        msgType = fix.MsgType()
        message.getHeader().getField(msgType)

        logger.info(f"Received message type: {msgType.getValue()}")

        if msgType.getValue() == fix.MsgType_ExecutionReport:
            self.handleExecutionReport(message)
        elif msgType.getValue() == fix.MsgType_OrderCancelReject:
            self.handleCancelReject(message)
        else:
            logger.warning(f"Unhandled message type: {msgType.getValue()}")

    def handleExecutionReport(self, message):
        """Process execution reports"""
        exec_report = fix44.ExecutionReport()
        exec_report.fromMessage(message)
        logger.info(f"Execution Report: {exec_report.toString()}")

    def handleCancelReject(self, message):
        """Process order cancel rejects"""
        reject = fix44.OrderCancelReject()
        reject.fromMessage(message)
        logger.warning(f"Cancel Reject: {reject.toString()}")

    def send_order(self, sessionID, symbol, side, quantity, price, ord_type=fix.OrdType_LIMIT):
        """Send NewOrderSingle (D) message"""
        try:
            message = fix44.NewOrderSingle()

            # Set standard header
            header = message.getHeader()
            header.setField(fix.SenderCompID("TRADING_SYSTEM"))
            header.setField(fix.TargetCompID("BROKER"))

            # Set order fields
            message.setField(fix.ClOrdID(self.get_clordid()))
            message.setField(fix.Symbol(symbol))
            message.setField(fix.Side(side))
            message.setField(fix.OrderQty(quantity))
            message.setField(fix.Price(price))
            message.setField(fix.OrdType(ord_type))
            message.setField(fix.HandlInst('1'))  # Automated execution

            # Set time in force (default: DAY)
            message.setField(fix.TimeInForce(fix.TimeInForce_DAY))

            fix.Session.sendToTarget(message, sessionID)
            logger.info(f"Order sent: {message.toString()}")
            return True
        except fix.InvalidMessage as e:
            logger.error(f"Failed to send order: {e}")
            return False

    def get_clordid(self):
        """Generate unique ClOrdID"""
        return f"ORD{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

def main():
    try:
        # Load FIX configuration
        settings = fix.SessionSettings("fix_config.cfg")
        application = FIXApplication()
        storefactory = fix.FileStoreFactory(settings)
        logfactory = fix.FileLogFactory(settings)
        initiator = fix.SocketInitiator(application, storefactory, settings, logfactory)

        logger.info("Starting FIX initiator...")
        initiator.start()

        # Wait for connection
        while not application.isLoggedOn():
            time.sleep(1)

        # Example: Send test order
        sessionID = fix.SessionID(
            "FIX.4.4",
            "TRADING_SYSTEM",
            "BROKER"
        )
        application.send_order(sessionID, "AAPL", fix.Side_BUY, 100, 150.25)

        # Keep connection alive
        while True:
            time.sleep(1)

    except (fix.ConfigError, fix.RuntimeError) as e:
        logger.error(f"FIX Error: {e}")
    except KeyboardInterrupt:
        logger.info("Shutting down FIX connection...")
        initiator.stop()
        logger.info("FIX initiator stopped.")

 

if __name__ == "__main__":

 main()
