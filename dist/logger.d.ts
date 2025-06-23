/**
 * Simple logger for Multi-Agent MCP Server
 */
export interface Logger {
    info(message: string, ...args: any[]): void;
    warn(message: string, ...args: any[]): void;
    error(message: string, ...args: any[]): void;
}
export declare const logger: Logger;
//# sourceMappingURL=logger.d.ts.map