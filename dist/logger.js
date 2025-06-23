/**
 * Simple logger for Multi-Agent MCP Server
 */
class ConsoleLogger {
    info(message, ...args) {
        console.log(`[INFO] ${message}`, ...args);
    }
    warn(message, ...args) {
        console.warn(`[WARN] ${message}`, ...args);
    }
    error(message, ...args) {
        console.error(`[ERROR] ${message}`, ...args);
    }
}
export const logger = new ConsoleLogger();
//# sourceMappingURL=logger.js.map